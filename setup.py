#!/usr/bin/env python

from distutils.core import setup
from commands import getoutput

version = getoutput('git describe --always') or '1.0'

setup(name='clonehub',
      version=version,
      description='GitHub backup script',
      author='Jakob Borg',
      author_email='jakob@nym.se',
      url='https://github.com/calmh/clonehub',
      scripts=['clonehub'],
     )
