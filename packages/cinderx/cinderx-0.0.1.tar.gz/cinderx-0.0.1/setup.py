#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cinderx",
    version="0.0.1",
    author="Meta Platforms",
    author_email="cinder@meta.com",
    description="High-performance Python runtime extensions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/facebookincubator/cinder",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=[
        setuptools.Extension(
            "cinderx",
            sources=["src/cinderx/cinderx.cpp"],
            extra_compile_args=["-std=c++11", "-Wall", "-Wextra"],
            language="c++",
        )
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires="==3.12.*",
)
