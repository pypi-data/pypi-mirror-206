# -*- coding: utf-8 -*-
# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.interface import classImplements

# visaplan:
from visaplan.plone.industrialsector.metadata.interfaces import (
    IHierarchicalCodeFormatted,
    )

# Local imports:
from .content.folderish_animation import FolderishAnimation

classImplements(FolderishAnimation, IHierarchicalCodeFormatted)
