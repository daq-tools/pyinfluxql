# -*- coding: utf-8 -*-
"""
    setup
    ~~~~~

    setup.py for PyInfluxQL
"""

from setuptools import setup, find_packages


def get_long_description():
    with open('README.rst') as f:
        readme = f.read()
    return readme

setup(
    name='pyinfluxql',
    version='0.0.1',
    url='https://github.com/jjmalina/pyinfluxql',
    author='Jeremiah Malina',
    author_email='me@jerem.io',
    description='A query generator for the InfluxDB SQL query syntax',
    long_description=get_long_description(),
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    tests_require=find_packages(include=['*-dev'])
)
