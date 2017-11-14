#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="Hangman1",
    version="0.0.0",
    author="Dmitry Karpov",
    author_email="dimakarp1996@yandex.ru",
    url="https://github.com/dimakarp1996/Hangman1",
    license="MIT",
    packages=[
        "Hangman1"
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pycodestyle",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pycodestyle",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
