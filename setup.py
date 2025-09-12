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


setup(
    name="zope.dublincore",
    version='6.0',
    url='http://github.com/zopefoundation/zope.dublincore',
    license='ZPL-2.1',
    description='Zope Dublin Core implementation',
    long_description=long_description,
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    keywords='metadata dublincore',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
    ],
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        'persistent',
        'pytz',
        'setuptools',
        'zope.annotation',
        'zope.component[zcml]',
        'zope.datetime',
        'zope.interface',
        'zope.lifecycleevent',
        'zope.location',
        'zope.schema',
        'zope.security[zcml]>=3.8',
    ],
    extras_require={
        'testing': testing_require,
        'test': tests_require,
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'zope.testing',
        ],
    },
    zip_safe=False,
)
