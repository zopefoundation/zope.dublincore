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
    with open(os.path.join(*path)) as f:
        return f.read() + '\n\n'


long_description = '\n\n'.join([
    read('README.rst'),
    read('CHANGES.rst')
])

testing_require = [
    'zope.testing >= 3.8',
    'zope.testrunner',
    'zope.configuration',
    'BTrees',
]

tests_require = testing_require + [
    # 'zope.annotation',
    'zope.publisher',
]


setup(
    name="zope.dublincore",
    version='4.3.0',
    url='http://github.com/zopefoundation/zope.dublincore',
    license='ZPL 2.1',
    description='Zope Dublin Core implementation',
    long_description=long_description,
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    keywords='metadata dublincore',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    include_package_data=True,
    install_requires=[
        'persistent',
        'pytz',
        'setuptools',
        'six',
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
        'docs': ['Sphinx', 'repoze.sphinx.autointerface'],
    },
    zip_safe=False,
)
