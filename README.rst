Prometheus middleware for ``aiohttp``
-------------------------------------

``aiohttp_prometheus`` adds support for exporting `prometheus metrics <https://promehteus.io>`__ to 
`aiohttp <https://github.com/aio-libs/aiohttp>`__ applications. It is implemented as a 
`aiohttp middleware <http://aiohttp.readthedocs.io/en/stable/web.html#middlewares>`__.

Currently, it exports the following metrics via the ``/metrics`` endpoint:

- ``request_latency_seconds``: Latency of a request in seconds. 
   
  + *Labels exported*: ``endpoint``, ``app_name``

- ``requests_total``: Request count. 
  
  + *Labels exported*: ``app_name``, ``method`` (HTTP method), ``endpoint``, ``http_status`` (HTTP status)

- ``requests_in_progress_total``: In progress requests.
  
  + *Labels exported*: ``app_name``, ``endpoint``, ``method`` (HTTP method)


Install
=======

I will be publishing to PyPI soon, but for now specifying the following in your ``requirements.txt`` file will 
install the ``master`` version of the package from github:

.. code::

    git+http://github.com/amitsaha/aiohttp-prometheus.git#egg=aiohttp_prometheus


Usage
=====

The ``aiohttp_prometheus`` package exports a single function ``setup_metrics(app, 'app_name')``
which takes in the following arguments:

- ``app``: The application object returned via ``web.Application()``
- The second argument is the web application name which identifies the web application and
  used to set the ``app_name`` label above

Briefly, the following is all you need to do to measure and export prometheus
metrics from your ``aiohttp`` web application:

.. code::

    from aiohttp_prometheus import setup_metrics
    from aiohttp import web
    app =  web.Application()
    setup_metrics(app, "mywebapp")

For complete examples, please see `examples <./examples>`__.

Discussions
===========

Please file a `issue <https://github.com/amitsaha/aiohttp-prometheus/issues/new>`__
to file a comment, report an issue or make a suggestion.
