##############################################################################
#
# Copyright (c) 2009 Zope Corporation and Contributors.
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
"""Tests annotatableadapter.

$Id: test_creatorannotator.py 101331 2009-06-29 20:58:01Z tseaver $
"""
import unittest

_marker = object()

class ZDCAnnotatableAdapterTests(unittest.TestCase):

    _registered = False

    def setUp(self):
        from zope.testing.cleanup import cleanUp
        cleanUp()

    def tearDown(self):
        from zope.testing.cleanup import cleanUp
        cleanUp()

    def _getTargetClass(self):
        from zope.dublincore.annotatableadapter import ZDCAnnotatableAdapter
        return ZDCAnnotatableAdapter

    def _registerAnnotations(self, dcdata=None):
        from zope.component import provideAdapter
        from zope.interface import Interface
        from zope.annotation.interfaces import IAnnotations
        from zope.dublincore.annotatableadapter import DCkey
        class _Annotations(dict):
            pass
        instance = _Annotations({DCkey: dcdata})
        def _factory(context):
            return instance
        if not self._registered:
            provideAdapter(_factory, (Interface, ), IAnnotations)
            self._registered = True
            return instance

    def _makeOne(self, context=_marker):
        if context is _marker:
            context = self._makeContext()
        return self._getTargetClass()(context)

    def _makeContext(self):
        class DummyContext(object):
            pass
        return DummyContext()

    def test_class_conforms_to_IWriteZopeDublinCore(self):
        from zope.interface.verify import verifyClass
        from zope.dublincore.interfaces import IWriteZopeDublinCore
        verifyClass(IWriteZopeDublinCore, self._getTargetClass())

    def test_instance_conforms_to_IWriteZopeDublinCore(self):
        from zope.interface.verify import verifyObject
        from zope.dublincore.interfaces import IWriteZopeDublinCore
        self._registerAnnotations()
        verifyObject(IWriteZopeDublinCore, self._makeOne())

    def test_ctor_wo_existing_DC_annotations(self):
        from zope.dublincore.annotatableadapter import DCkey
        self._registerAnnotations()
        context = self._makeContext()
        adapter = self._makeOne(context)
        self.assertEqual(adapter.annotations[DCkey], None)
        self.assertEqual(adapter._mapping, {})

    def test_ctor_w_existing_DC_annotations(self):
        from zope.dublincore.annotatableadapter import DCkey
        DCDATA = {'title': 'TITLE'}
        self._registerAnnotations(DCDATA)
        context = self._makeContext()
        adapter = self._makeOne(context)
        self.assertEqual(adapter.annotations, None)
        self.assertEqual(adapter._mapping, DCDATA)

    def test__changed_wo_existing_DC_annotations(self):
        from zope.dublincore.annotatableadapter import DCkey
        annotations = self._registerAnnotations()
        context = self._makeContext()
        adapter = self._makeOne(context)
        adapter._mapping['title'] = 'NEW TITLE'
        adapter._changed()
        self.assertEqual(annotations[DCkey]['title'], 'NEW TITLE')

    def test__changed_w_existing_DC_annotations(self):
        from zope.dublincore.annotatableadapter import DCkey
        DCDATA = {'title': 'TITLE'}
        annotations = self._registerAnnotations(DCDATA)
        context = self._makeContext()
        adapter = self._makeOne(context)
        adapter._changed()
        self.assertEqual(annotations[DCkey]['title'], 'TITLE') #unchanged

def test_suite():
    return unittest.TestSuite((
            unittest.makeSuite(ZDCAnnotatableAdapterTests),
        ))

