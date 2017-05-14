from aiohttp import web
from aiohttp_prometheus import setup_metrics
import asyncio

@asyncio.coroutine
def error_middleware(app, handler):

    @asyncio.coroutine
    def middleware_handler(request):
        try:
            response = yield from handler(request)
            return response
        except web.HTTPException as ex:
            resp = web.Response(body=str(ex), status=ex.status)
            return resp
        except Exception as ex:
            resp = web.Response(body=str(ex), status=500)
            return resp

    return middleware_handler

async def test(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def test1(request):
    1/0

if __name__ == '__main__':
    app = web.Application(middlewares=[error_middleware])
    setup_metrics(app, "webapp_1")
    app.router.add_get('/test', test)
    app.router.add_get('/test1', test1)

    web.run_app(app, port=8080)
