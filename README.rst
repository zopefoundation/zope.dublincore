zope.dublincore
===============

.. image:: https://github.com/zopefoundation/zope.dublincore/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/zopefoundation/zope.dublincore/actions/workflows/tests.yml

.. image:: https://readthedocs.org/projects/zopedublincore/badge/?version=latest
   :target: http://zopedublincore.readthedocs.org/en/latest/
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/zope.dublincore.svg
   :target: https://pypi.python.org/pypi/zope.dublincore/
   :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/zope.dublincore.svg
   :target: https://pypi.org/project/zope.dublincore/
   :alt: Supported Python versions

.. image:: https://coveralls.io/repos/github/zopefoundation/zope.dublincore/badge.svg?branch=master
   :target: https://coveralls.io/github/zopefoundation/zope.dublincore?branch=master
   :alt: Code Coverage


This package provides a Dublin Core support for Zope-based web
applications.  This includes:

* an ``IZopeDublinCore`` interface definition that can be implemented
  by objects directly or via an adapter to support DublinCore
  metadata.

* an ``IZopeDublinCore`` adapter for annotatable objects (objects
  providing ``IAnnotatable`` from ``zope.annotation``).

* a partial adapter for objects that already implement some of the
  ``IZopeDublinCore`` API,

* a "Metadata" browser page (which by default appears in the ZMI),

* subscribers to various object lifecycle events that automatically
  set the created and modified date and some other metadata.

Complete documentation is hosted at https://zopedublincore.readthedocs.io/
