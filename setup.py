##############################################################################
#
# Copyright (c) 2007 Zope Corporation and Contributors.
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
"""Setup for zope.dublincore package

$Id$
"""
from setuptools import setup, find_packages

long_description = (open('README.txt').read() +
                    '\n\n' +
                    open('CHANGES.txt').read())

setup(
    name="zope.dublincore",
    version = '3.4.1dev',
    url='http://pypi.python.org/pypi/zope.dublincore',
    license='ZPL 2.1',
    description='Zope Dublin Core implementation',
    long_description=long_description,
    author='Zope Corporation and Contributors',
    author_email='zope3-dev@zope.org',

    packages=find_packages('src'),
    package_dir={'':'src'},
    namespace_packages=['zope'],
    include_package_data=True,
    install_requires = ['setuptools',
                        'zope.annotation',
                        'zope.component',
                        'zope.interface',
                        # required for testing
                        'zope.testing',
                        'zope.security',
                        'zope.app.testing',
                        ],
    zip_safe = False
    )
