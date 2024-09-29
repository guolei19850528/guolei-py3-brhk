#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="guolei-py3-brhk",
    version="2.0.0",
    description="天津博瑞皓科 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guolei19850528/guolei_py3_brhk",
    author="guolei",
    author_email="174000902@qq.com",
    license="MIT",
    keywors=["brhk", "博瑞皓科", "天津博瑞皓科"],
    packages=setuptools.find_packages('./'),
    install_requires=[
        "guolei-py3-requests",
        "addict",
        "retrying",
        "jsonschema",
    ],
    python_requires='>=3.0',
    zip_safe=False
)
