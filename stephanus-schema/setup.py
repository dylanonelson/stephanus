#!/usr/bin/env python

from distutils.core import setup

setup(name='Stephanus Schema',
      version='0.1dev',
      description='JSON Schema for Platonic texts',
      author='Dylan Nelson',
      author_email='dylanonelson@gmail.com',
      install_requires=[
        'jsonschema',
        'jsonref',
      ],
      packages=['stephanus_schema'],
     )
