##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
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
"""Test Zope's Dublin Core implementation
"""

from unittest import TestCase


class Test(TestCase):

    def testImplementa(self):
        from zope.interface.verify import verifyObject

        from zope.dublincore.interfaces import IZopeDublinCore
        verifyObject(IZopeDublinCore, self.dc)

    def _Test__new(self):
        from zope.dublincore.zopedublincore import ZopeDublinCore
        return ZopeDublinCore()

    def setUp(self):
        self.dc = self._Test__new()

    def __testGetQualified(self, name, values):
        ovalues = getattr(self.dc, 'getQualified' + name)()

        ivalues = list(values)
        ivalues.sort()
        ovalues = list(ovalues)
        ovalues.sort()
        self.assertEqual(ovalues, ivalues)

    def __testQualified(self, name,
                        values=[
                            ('', 'blah blah'),
                            ('old', 'bleep bleep'),
                            ('old', 'bleep bleep \u1111'),
                            ('foo\u1111', 'bleep bleep'),
                        ]):
        getattr(self.dc, 'setQualified' + name)(values)
        self.__testGetQualified(name, values)

    def testOtherQualified(self):
        for name in ('Sources', 'Relations', 'Coverages'):
            self.__testQualified(name)

    def testScalars(self):
        for qname, mname, pname in (
                ('Titles', 'Title', 'title'),
                ('Descriptions', 'Description', 'description'),
                ('Publishers', 'Publisher', 'publisher'),
                ('Types', 'Type', 'type'),
                ('Formats', 'Format', 'format'),
                ('Identifiers', 'Identifier', 'identifier'),
                ('Languages', 'Language', 'language'),
                ('Rights', 'Rights', 'rights'),
        ):
            self.__testQualified(qname)
            dc = self.dc
            self.assertEqual(getattr(dc, pname), 'blah blah')
            self.assertEqual(getattr(dc, mname)(), 'blah blah')

            self.assertRaises(Exception, setattr, dc, pname, b'foo')
            setattr(dc, pname, 'foo')
            self.assertEqual(getattr(dc, pname), 'foo')
            self.assertEqual(getattr(dc, mname)(), 'foo')
            self.__testGetQualified(qname,
                                    [('', 'foo'),
                                     ('old', 'bleep bleep'),
                                     ('old', 'bleep bleep \u1111'),
                                     ('foo\u1111', 'bleep bleep'),
                                     ]
                                    )

    def testSequences(self):
        for qname, mname, pname in (
            ('Creators', 'Creator', 'creators'),
            ('Subjects', 'Subject', 'subjects'),
            ('Contributors', 'Contributors', 'contributors'),
        ):
            self.__testQualified(qname, [('', 'foo'),
                                         ('', 'bar'),
                                         ('', 'baz'),
                                         ('', 'baz\u1111'),
                                         ('old', 'bleep bleep'),
                                         ('old', 'bleep bleep \u1111'),
                                         ('foo\u1111', 'bleep bleep'),
                                         ]
                                 )
            dc = self.dc

            v = getattr(dc, pname)
            v = list(v)
            v.sort()
            self.assertEqual(v, ['bar', 'baz', 'baz\u1111', 'foo'])

            v = getattr(dc, mname)()
            v = list(v)
            v.sort()
            self.assertEqual(v, ['bar', 'baz', 'baz\u1111', 'foo'])

            self.assertRaises(Exception, setattr, dc, pname, b'foo')
            self.assertRaises(Exception, setattr, dc, pname, [b'foo'])

            setattr(dc, pname, ['high', 'low', 'spam', 'eggs', 'ham', ])

            v = getattr(dc, pname)
            v = list(v)
            v.sort()
            self.assertEqual(v, ['eggs', 'ham', 'high', 'low', 'spam'])

            v = getattr(dc, mname)()
            v = list(v)
            v.sort()
            self.assertEqual(v, ['eggs', 'ham', 'high', 'low', 'spam'])

            self.__testGetQualified(qname,
                                    [('', 'high'),
                                     ('', 'low'),
                                     ('', 'spam'),
                                     ('', 'eggs'),
                                     ('', 'ham'),
                                     ('old', 'bleep bleep'),
                                     ('old', 'bleep bleep \u1111'),
                                     ('foo\u1111', 'bleep bleep'),
                                     ]
                                    )

    def testDates(self):
        self.__testQualified('Dates', [
            ('', '1990-01-01'),
            ('Created', '1980-10-01T23:11:10-04:00'),
            ('Modified', '2002-10-01T12:09:22-04:00'),
            ('Effective', '2002-10-09T00:00:00-04:00'),
            ('Expires', '2002-10-16T00:00:00-04:00'),
            ('xxx', '2000-07-04'),
            ('xxx', '2001-12-31'),
            ('foo \u1111', '2001-12-31'),
        ])

        from zope.datetime import parseDatetimetz

        dc = self.dc
        self.assertEqual(dc.created,
                         parseDatetimetz('1980-10-01T23:11:10-04:00'))
        self.assertEqual(dc.modified,
                         parseDatetimetz('2002-10-01T12:09:22-04:00'))
        self.assertEqual(dc.effective,
                         parseDatetimetz('2002-10-09T00:00:00-04:00'))
        self.assertEqual(dc.expires,
                         parseDatetimetz('2002-10-16T00:00:00-04:00'))

        self.assertEqual(dc.Date(), '1990-01-01')
        self.assertEqual(dc.CreationDate(), '1980-10-01T23:11:10-04:00')
        self.assertEqual(dc.ModificationDate(), '2002-10-01T12:09:22-04:00')
        self.assertEqual(dc.EffectiveDate(), '2002-10-09T00:00:00-04:00')
        self.assertEqual(dc.ExpirationDate(), '2002-10-16T00:00:00-04:00')

        dt = parseDatetimetz('2002-10-03T14:51:55-04:00')

        dc.modified = dt

        self.assertRaises(Exception, setattr, dc, 'modified', 'foo')

        modified = [qv[1]
                    for qv in dc.getQualifiedDates()
                    if qv[0] == 'Modified']

        self.assertEqual(
            len(modified),
            1,
            "should be only one: %r" % modified
        )

        self.assertEqual(parseDatetimetz(modified[0]), dt)

        modified = dc.ModificationDate()
        self.assertEqual(parseDatetimetz(modified), dt)
