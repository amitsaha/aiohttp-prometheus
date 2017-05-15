from prometheus_client import Counter, Gauge, Histogram, CONTENT_TYPE_LATEST
import time
import asyncio
from aiohttp import web
import prometheus_client


def prom_middleware(app_name):
    @asyncio.coroutine
    def factory(app, handler):
        @asyncio.coroutine
        def middleware_handler(request):
            try:
                request['start_time'] = time.time()
                app['REQUEST_IN_PROGRESS'].labels(
                            app_name, request.path, request.method).inc()
                response = yield from handler(request)
                resp_time = time.time() - request['start_time']
                request.app['REQUEST_LATENCY'].labels(app_name, request.path).observe(resp_time)
                request.app['REQUEST_IN_PROGRESS'].labels(app_name, request.path, request.method).dec()
                request.app['REQUEST_COUNT'].labels(
                            app_name, request.method, request.path, response.status).inc()
                return response
            except Exception as ex:
                raise
        return middleware_handler
    return factory


async def metrics(request):
    resp = web.Response(body=prometheus_client.generate_latest())
    resp.content_type = CONTENT_TYPE_LATEST
    return resp


def setup_metrics(app, app_name):
    app['REQUEST_COUNT'] = Counter(
      'request_count', 'App Request Count',
      ['app_name', 'method', 'endpoint', 'http_status']
    )
    app['REQUEST_LATENCY'] = Histogram(
        'request_latency_seconds', 'Request latency',
        ['app_name', 'endpoint']
    )

    app['REQUEST_IN_PROGRESS'] = Gauge(
        'requests_in_progress', 'Requests in progress',
        ['app_name', 'endpoint', 'method']
    )

    app.middlewares.insert(0, prom_middleware(app_name))
    app.router.add_get("/metrics", metrics)
