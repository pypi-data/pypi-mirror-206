from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'package'
LONG_DESCRIPTION = 'A package'

# Setting up
setup(
    name="pendazz",
    version=VERSION,
    author="code4321",
    author_email="codetesting0003@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
)