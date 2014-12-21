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
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.dublincore package
"""
from setuptools import setup, find_packages
import os.path

def read(*path):
    return open(os.path.join(*path)).read() + '\n\n'

def alltests():
    import os
    import sys
    import unittest
    # use the zope.testrunner machinery to find all the
    # test suites we've put under ourselves
    import zope.testrunner.find
    import zope.testrunner.options
    here = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
    args = sys.argv[:]
    defaults = ["--test-path", here]
    options = zope.testrunner.options.get_options(args, defaults)
    suites = list(zope.testrunner.find.find_suites(options))
    return unittest.TestSuite(suites)

long_description = (
    '.. contents::\n\n' +
    '========\n' +
    'Overview\n' +
    '========\n' +
    read('README.rst') +
    read('src', 'zope', 'dublincore', 'property.txt') +
    read('src', 'zope', 'dublincore', 'tests', 'partial.txt') +
    read('src', 'zope', 'dublincore', 'tests', 'timeannotators.txt') +
    read('CHANGES.rst')
    )

setup(
    name="zope.dublincore",
    version='4.0.1',
    url='http://pypi.python.org/pypi/zope.dublincore',
    license='ZPL 2.1',
    description='Zope Dublin Core implementation',
    long_description=long_description,
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        ],

    packages=find_packages('src'),
    package_dir={'':'src'},
    namespace_packages=['zope'],
    include_package_data=True,
    extras_require=dict(
        test=['zope.testing >= 3.8',
              'zope.testrunner',
              'zope.annotation',
              'zope.configuration',
              ]
        ),
    install_requires = [
        'pytz',
        'setuptools',
        'six',
        'zope.component[zcml]',
        'zope.datetime',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.location',
        'zope.schema',
        'zope.security[zcml]>=3.8',
        ],
    tests_require = [
        'zope.testing',
        'zope.testrunner',
        'zope.annotation',
        'zope.configuration'],
    test_suite = '__main__.alltests',
    zip_safe = False
    )
