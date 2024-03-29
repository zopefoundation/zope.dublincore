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
"""Object that takes care of annotating the dublin core creator field.
"""
from zope.security.management import queryInteraction
from zope.security.proxy import removeSecurityProxy

from zope.dublincore.interfaces import IZopeDublinCore


def CreatorAnnotator(object, event=None):
    """Update Dublin-Core creator property"""
    if event is None:
        # annotator was only called the event as only argument
        object = object.object
    dc = IZopeDublinCore(object, None)
    # Principals that can create objects do not necessarily have
    # 'zope.app.dublincore.change' permission.
    # https://bugs.launchpad.net/zope3/+bug/98124
    dc = removeSecurityProxy(dc)
    if dc is None:
        return

    # Try to find a principal for that one. If there
    # is no principal then we don't touch the list
    # of creators.
    interaction = queryInteraction()
    if interaction is not None:
        for participation in interaction.participations:
            if participation.principal is None:
                continue
            principalid = participation.principal.id
            if principalid not in dc.creators:
                dc.creators = dc.creators + (str(principalid), )
