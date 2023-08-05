# -*- coding: utf-8 -*-
import setuptools
import TrimPypi

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read().replace(
        "./docs/", "https://github.com/TriM-Organization/TrimPypi/blob/master/README.md"
    )

setuptools.setup(
    name="TrimPypi",
    version=TrimPypi.__version__,
    author="bgArray",
    author_email="TriM-Organization@hotmail.com",
    description="Pypi上传工具本地配套文件初始化管理。\n"
    "Local supporting file initialization management for Pypi upload tool.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TriM-Organization/TrimPypi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Chinese (Simplified)",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
