##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# https://zopetoolkit.readthedocs.io/
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.dublincore package
"""
import os.path

from setuptools import setup


def read(*path):
    with open(os.path.join(*path)) as f:
        return f.read() + '\n\n'


long_description = '\n\n'.join([
    read('README.rst'),
    read('CHANGES.rst')
])

testing_require = [
    'zope.testing >= 3.8',
    'zope.testrunner >= 6.4',
    'zope.configuration',
    'BTrees',
]

tests_require = testing_require + [
    'zope.publisher',
]

# See pyproject.toml for package metadata
setup()
