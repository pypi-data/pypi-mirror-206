#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name="Log10",
    version="0.0.5",
    description="Log10 LLM data management",
    author="Log10 team",
    author_email="team@log10.io",
    url="",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    extras_require={
        "bigquery": ["google-cloud-bigquery"],
    },
)
