#!/usr/bin/env python

from distutils.core import setup
import py2exe

setup(
  console=["loader.py"],
  zipfile=None
)