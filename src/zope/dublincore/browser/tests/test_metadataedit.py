import unittest

import zope.annotation.interfaces
from zope.component.testing import PlacelessSetup
from zope.publisher.browser import TestRequest

import zope.dublincore.testing
from zope.dublincore.browser.metadataedit import MetaDataEdit


@zope.interface.implementer(zope.annotation.interfaces.IAnnotations)
class DummyContext(dict):
    """A dummy class which can store annotations."""


class MetaDataEditTests(PlacelessSetup, unittest.TestCase):
    """Testing ..metadataedit.MetaDataEdit."""

    def setUp(self):
        super().setUp()
        zope.dublincore.testing.setUpDublinCore()

    def test_metadataedit__MetaDataEdit__edit__1(self):
        """It stores DC request values on the context."""
        view = MetaDataEdit()
        request = TestRequest(
            form={'dctitle': 'Test', 'dcdescription': 'Testing'})
        view.context = DummyContext()
        view.request = request
        result = view.edit()
        self.assertEqual({
            'message': 'Changed data ${datetime}',
            'dctitle': 'Test',
            'dcdescription': 'Testing',
            'modified': '',
            'created': '',
            'creators': ()
        }, result)

        self.assertEqual({
            'zope.app.dublincore.ZopeDublinCore': {
                'Title': ('Test',),
                'Description': ('Testing',)}}, view.context)
