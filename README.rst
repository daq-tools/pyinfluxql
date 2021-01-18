##########
PyInfluxQL
##########

.. image:: https://github.com/daq-tools/pyinfluxql/workflows/Tests/badge.svg
    :target: https://github.com/daq-tools/pyinfluxql/actions?workflow=Tests

.. image:: https://img.shields.io/pypi/pyversions/pyinfluxql.svg
    :target: https://python.org

.. image:: https://img.shields.io/pypi/v/pyinfluxql.svg
    :target: https://pypi.org/project/pyinfluxql/

.. image:: https://img.shields.io/pypi/dm/pyinfluxql.svg
    :target: https://pypi.org/project/pyinfluxql/

.. image:: https://img.shields.io/pypi/status/pyinfluxql.svg
    :target: https://pypi.org/project/pyinfluxql/

.. image:: https://img.shields.io/pypi/l/pyinfluxql.svg
    :target: https://pypi.org/project/pyinfluxql/


*****
About
*****
A query generator for the SQL dialect of the `Influx Query Language (InfluxQL)`_.
Like SQLAlchemy but for InfluxDB. Consider this an experimental WIP.

.. _Influx Query Language (InfluxQL): https://docs.influxdata.com/influxdb/v1.8/query_language/


********
Synopsis
********
.. code-block:: python

    from influxdb import InfluxDBClient
    from pyinfluxql import Engine, Query, Mean

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
    engine = Engine(client)
    query = Query(Mean('value')).from_('cpu_load') \
        .where(time__gt=datetime.now() - timedelta(1))
        .group_by(time=timedelta(hours=1))
    engine.execute(query)


*****
Tests
*****
How to invoke the test suite.

Using Tox
=========
Run InfluxDB within Docker::

    docker run -it --rm --publish 8086:8086 influxdb:1.8.3

Run ``tox``::

    tox


Using sandbox
=============
Alternatively, setup package in development mode::

    python3 -mvenv .venv
    source .venv/bin/activate
    pip install --editable=.[test]

Run ``pytest``::

    py.test tests -vvv
