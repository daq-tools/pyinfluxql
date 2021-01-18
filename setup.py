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
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        "six>=1.9.0,<2",
        "influxdb>=2.8.0,<3",
    ],
    extras_require={
        "test": [
            "pytest>=2.7.2,<3",
        ]
    },
)
