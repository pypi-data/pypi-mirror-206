"""
visaplan.plone.animations: @@landing_path for FolderishAnimations

This variant is used in case visaplan.plone.structures in installed,
which provides the @@info view for (parent) folders.

For the more basic variant, see ./lapa.py
"""

# Python compatibility:
from __future__ import absolute_import

# Zope:
from Products.Five.browser import BrowserView
from zope.interface import implements

# Plone:
from plone.uuid.interfaces import IUUID

# visaplan:
from visaplan.plone.search.interfaces import ILandingPath

# Local imports:
from visaplan.plone.animations.utils import landingpath


class LandingPath(BrowserView):
    implements(ILandingPath)
    def __call__(self):
        """
        Return the visible URL for use for search results lists

        From visaplan.plone.structures, we have the @@info view, which allows
        us to present our FolderishAnimation object even to users who lack view
        permission.
        """
        context = self.context
        return landingpath(context)
