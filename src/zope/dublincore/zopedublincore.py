##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
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
"""Zope's Dublin Core Implementation
"""
from datetime import datetime

from zope.datetime import parseDatetimetz
from zope.interface import implementer

from zope.dublincore.interfaces import IZopeDublinCore


class SimpleProperty:

    def __init__(self, name):
        self.__name__ = name


class ScalarProperty(SimpleProperty):

    def __get__(self, inst, klass):
        if inst is None:
            return self
        data = inst._mapping.get(self.__name__, ())
        if data:
            return data[0]
        else:
            return ''

    def __set__(self, inst, value):
        if not isinstance(value, str):
            raise TypeError("Element must be str")
        dict = inst._mapping
        __name__ = self.__name__
        inst._changed()
        dict[__name__] = (value, ) + dict.get(__name__, ())[1:]


def _scalar_get(inst, name):
    data = inst._mapping.get(name, ())
    if data:
        return data[0]
    else:
        return ''


class DateProperty(ScalarProperty):

    def __get__(self, inst, klass):
        if inst is None:
            return self
        data = inst._mapping.get(self.__name__, ())
        if data:
            return parseDatetimetz(data[0])
        else:
            return None

    def __set__(self, inst, value):
        if not isinstance(value, datetime):
            raise TypeError("Element must be %s", datetime)

        value = value.isoformat('T')
        if isinstance(value, bytes):
            value = value.decode('ascii')

        super().__set__(inst, value)


class SequenceProperty(SimpleProperty):

    def __get__(self, inst, klass):
        if inst is None:
            return self

        return inst._mapping.get(self.__name__, ())

    def __set__(self, inst, value):
        value = tuple(value)
        for v in value:
            if not isinstance(v, str):
                raise TypeError("Elements must be str")
        inst._changed()
        inst._mapping[self.__name__] = value


@implementer(IZopeDublinCore)
class ZopeDublinCore:
    """Zope Dublin Core Mixin

    Subclasses should define either `_changed()` or `_p_changed`.

    Just mix with `Persistence` to get a persistent version.
    """

    def __init__(self, mapping=None):
        if mapping is None:
            mapping = {}
        self._mapping = mapping

    def _changed(self):
        self._p_changed = True

    title = ScalarProperty('Title')

    def Title(self):
        """See `IZopeDublinCore`"""
        return self.title

    creators = SequenceProperty('Creator')

    def Creator(self):
        """See `IZopeDublinCore`"""
        return self.creators

    subjects = SequenceProperty('Subject')

    def Subject(self):
        """See `IZopeDublinCore`"""
        return self.subjects

    description = ScalarProperty('Description')

    def Description(self):
        """See `IZopeDublinCore`"""
        return self.description

    publisher = ScalarProperty('Publisher')

    def Publisher(self):
        """See IZopeDublinCore"""
        return self.publisher

    contributors = SequenceProperty('Contributor')

    def Contributors(self):
        """See `IZopeDublinCore`"""
        return self.contributors

    def Date(self):
        """See IZopeDublinCore"""
        return _scalar_get(self, 'Date')

    created = DateProperty('Date.Created')

    def CreationDate(self):
        """See `IZopeDublinCore`"""
        return _scalar_get(self, 'Date.Created')

    effective = DateProperty('Date.Effective')

    def EffectiveDate(self):
        """See `IZopeDublinCore`"""
        return _scalar_get(self, 'Date.Effective')

    expires = DateProperty('Date.Expires')

    def ExpirationDate(self):
        """See `IZopeDublinCore`"""
        return _scalar_get(self, 'Date.Expires')

    modified = DateProperty('Date.Modified')

    def ModificationDate(self):
        """See `IZopeDublinCore`"""
        return _scalar_get(self, 'Date.Modified')

    type = ScalarProperty('Type')

    def Type(self):
        """See `IZopeDublinCore`"""
        return self.type

    format = ScalarProperty('Format')

    def Format(self):
        """See `IZopeDublinCore`"""
        return self.format

    identifier = ScalarProperty('Identifier')

    def Identifier(self):
        """See `IZopeDublinCore`"""
        return self.identifier

    language = ScalarProperty('Language')

    def Language(self):
        """See `IZopeDublinCore`"""
        return self.language

    rights = ScalarProperty('Rights')

    def Rights(self):
        """See `IZopeDublinCore`"""
        return self.rights

    def setQualifiedTitles(self, qualified_titles):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Title', qualified_titles)

    def setQualifiedCreators(self, qualified_creators):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Creator', qualified_creators)

    def setQualifiedSubjects(self, qualified_subjects):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Subject', qualified_subjects)

    def setQualifiedDescriptions(self, qualified_descriptions):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Description', qualified_descriptions)

    def setQualifiedPublishers(self, qualified_publishers):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Publisher', qualified_publishers)

    def setQualifiedContributors(self, qualified_contributors):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Contributor', qualified_contributors)

    def setQualifiedDates(self, qualified_dates):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Date', qualified_dates)

    def setQualifiedTypes(self, qualified_types):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Type', qualified_types)

    def setQualifiedFormats(self, qualified_formats):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Format', qualified_formats)

    def setQualifiedIdentifiers(self, qualified_identifiers):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Identifier', qualified_identifiers)

    def setQualifiedSources(self, qualified_sources):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Source', qualified_sources)

    def setQualifiedLanguages(self, qualified_languages):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Language', qualified_languages)

    def setQualifiedRelations(self, qualified_relations):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Relation', qualified_relations)

    def setQualifiedCoverages(self, qualified_coverages):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Coverage', qualified_coverages)

    def setQualifiedRights(self, qualified_rights):
        """See `IWritableDublinCore`"""
        return _set_qualified(self, 'Rights', qualified_rights)

    def getQualifiedTitles(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Title')

    def getQualifiedCreators(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Creator')

    def getQualifiedSubjects(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Subject')

    def getQualifiedDescriptions(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Description')

    def getQualifiedPublishers(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Publisher')

    def getQualifiedContributors(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Contributor')

    def getQualifiedDates(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Date')

    def getQualifiedTypes(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Type')

    def getQualifiedFormats(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Format')

    def getQualifiedIdentifiers(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Identifier')

    def getQualifiedSources(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Source')

    def getQualifiedLanguages(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Language')

    def getQualifiedRelations(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Relation')

    def getQualifiedCoverages(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Coverage')

    def getQualifiedRights(self):
        """See `IStandardDublinCore`"""
        return _get_qualified(self, 'Rights')


def _set_qualified(self, name, qvalue):
    data = {}
    dict = self._mapping

    for qualification, value in qvalue:
        data[qualification] = data.get(qualification, ()) + (value, )

    self._changed()
    for qualification, values in data.items():
        qname = qualification and (name + '.' + qualification) or name
        dict[qname] = values


def _get_qualified(self, name):
    result = []
    for aname, avalue in self._mapping.items():

        if aname == name:
            qualification = ''
            for value in avalue:
                result.append((qualification, value))

        elif aname.startswith(name):
            qualification = aname[len(name) + 1:]
            for value in avalue:
                result.append((qualification, value))

    return tuple(result)


__doc__ = ZopeDublinCore.__doc__ + __doc__
