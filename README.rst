``zope.dublincore``
===================

.. image:: https://pypip.in/version/zope.dublincore/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/zope.dublincore/
    :alt: Latest Version

.. image:: https://travis-ci.org/zopefoundation/zope.dublincore.png?branch=master
        :target: https://travis-ci.org/zopefoundation/zope.dublincore

.. image:: https://readthedocs.org/projects/zopedublincore/badge/?version=latest
        :target: http://zopedublincore.readthedocs.org/en/latest/
        :alt: Documentation Status

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
