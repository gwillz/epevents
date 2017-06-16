#!/usr/bin/env python
from setuptools import setup
import os

def get_long_description(fname):
    try:
        import pypandoc
        return pypandoc.convert(fname, 'rst')
    except:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='epevents',
      version="0.1",
      description="A C# style event library",
      long_description=get_long_description('README.md'),
      author='Gwilyn Saunders / Masaaki Shibata',
      author_email='gwilyn.saunders@mk2es.com.au',
      url='https://git.mk2es.com.au/mk2/epevents',
      packages=['epevents'],
      classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Operating System :: OS Independent",
      ],
)
