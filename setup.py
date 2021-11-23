#!/usr/bin/env python

from distutils.core import setup
from micro import __version__

setup(name='micro_framework',
      version=__version__,
      description='Python microservice framework',
      author='svtter',
      author_email='svtter@163.com',
      url='',
      packages=['micro', 'tests'],
     )