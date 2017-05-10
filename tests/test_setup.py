from aiohttp.test_utils import _create_app_mock
from aiohttp_prometheus import setup_metrics


def test_setup_middlware():
    app = _create_app_mock()
    app.middlewares = []
    setup_metrics(app, 'test_app')
    assert len(app.middlewares) == 1
