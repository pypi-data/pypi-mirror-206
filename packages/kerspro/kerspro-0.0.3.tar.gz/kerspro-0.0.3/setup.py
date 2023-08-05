from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'package'
LONG_DESCRIPTION = 'A package'

# Setting up
setup(
    name="kerspro",
    version=VERSION,
    author="nandan_6",
    author_email="nandanpadia@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
)