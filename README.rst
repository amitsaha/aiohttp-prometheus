Prometheus middleware for ``aiohttp``
-------------------------------------

``aiohttp_prometheus`` adds support for exporting `prometheus metrics <https://promehteus.io>`__ to `aiohttp <https://github.com/aio-libs/aiohttp>`__ applications. It is implemented as a `aiohttp middleware <http://aiohttp.readthedocs.io/en/stable/web.html#middlewares>`__.

Currently, it exports the following metrics:

- ``request_latency_seconds``: Latency of a request. Labels exported: ``endpoint``, ``app_name``
- ``request_count``: Request count. Labels exported: ``app_name``, ``method`` (HTTP method), ``endpoint``, ``http_status`` (HTTP status)
- ``requests_in_progress``: In progress requests. Labels: ``app_name``, ``endpoint``, ``method`` (HTTP method)

In addition, the ``/metrics`` endpoint exports these metrics.

Install
=======

TODO


Usage
=====

.. code::

    from aiohttp_prometheus import setup_metrics
    app =  web.Application()
    setup_metrics(app, "mywebapp")
