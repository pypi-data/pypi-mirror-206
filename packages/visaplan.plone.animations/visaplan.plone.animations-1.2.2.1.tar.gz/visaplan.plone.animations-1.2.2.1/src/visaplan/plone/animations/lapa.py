"""
visaplan.plone.animations: @@landing_path for FolderishAnimations

Currently our view to folderish animations doesn't work well when embedded into
HTML pages, so we usually open them in a new (tab or) window, using the
'onlyme' view.

However, the visaplan.plone.structures provides an @@info view for (parent)
folders, which currently supports FolderishAnimations explicitly;
see ./lapainfo.py and, to take into accout @@mainmenu as well, ./lapamenu.py.
"""
# Python compatibility:
from __future__ import absolute_import

# Zope:
from Products.Five.browser import BrowserView
from zope.interface import implements

# visaplan:
from visaplan.plone.search.interfaces import ILandingPath


class LandingPath(BrowserView):
    implements(ILandingPath)
    def __call__(self):
        """
        Return the visible URL for use for search results lists

        For FolderishAnimations, we direct to the .../onlyme view currently,
        which doesn't contain the platform requites but only the animation
        itself and thus should probably be opened in a new window
        (target=_blank); there is currently no support for doing this
        automatically, though.
        """
        return self.context.absolute_url_path() + '/onlyme'
