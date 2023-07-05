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
"""Objects that take care of annotating dublin core meta data times
"""
from datetime import datetime

import pytz

from zope.security.proxy import removeSecurityProxy

from zope.dublincore.interfaces import IZopeDublinCore


_NOW = None


def _now():
    if _NOW is None:
        return datetime.now(pytz.utc)
    return _NOW


def ModifiedAnnotator(object, event=None):
    if event is None:
        # annotator was only called the event as only argument
        object = object.object
    dc = IZopeDublinCore(object, None)
    if dc is not None:
        # Principals that can modify objects do not necessary have permissions
        # to arbitrarily modify DC data, see issue 373
        dc = removeSecurityProxy(dc)
        dc.modified = _now()


def CreatedAnnotator(object, event=None):
    if event is None:
        # annotator was only called the event as only argument
        object = object.object
    dc = IZopeDublinCore(object, None)
    if dc is not None:
        # Principals that can create objects do not necessary have permissions
        # to arbitrarily modify DC data, see issue 373
        dc = removeSecurityProxy(dc)
        now = _now()
        dc.created = now
        dc.modified = now
