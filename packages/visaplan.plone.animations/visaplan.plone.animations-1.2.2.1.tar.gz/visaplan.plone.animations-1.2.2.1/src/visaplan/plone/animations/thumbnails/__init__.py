"""
visaplan.plone.animations: @@getThumbnailPath for FolderishAnimations
"""

# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.interface import implements

# visaplan:
from visaplan.plone.staticthumbnails.browser.dx import \
    FromImageAttribute as Base
from visaplan.plone.staticthumbnails.interfaces import IDedicatedThumbnail


class FromImageAttribute(Base):
    # see (gf): ../../../../../visaplan.plone.staticthumbnails/src/visaplan/plone/staticthumbnails/browser/dx.py
    def getDefaultThumbnailPath(self):
        return '/++resource++unitracc-images/picto_media_animation_m.png'
