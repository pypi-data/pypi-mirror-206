# -*- coding: utf-8 -*-
# Python compatibility:
from __future__ import absolute_import

from importlib_metadata import PackageNotFoundError, version

# Setup tools:
from packaging.version import parse as parse_version

# Standard library:
from collections import Counter

# Zope:
from Products.CMFCore.utils import getToolByName
from zope.interface import implementer

# Plone:
from plone.app.upgrade.utils import loadMigrationProfile
from Products.CMFPlone.interfaces import INonInstallable

try:
    _vps_v = version('visaplan.plone.search')
except PackageNotFoundError:
    getExcludeFromNav = 'getExcludeFromNav'  # WIP: change index name
else:
    _vps_v = parse_version(_vps_v)
    if _vps_v < parse_version('1.7'):
        raise ImportError('Found visaplan.plone.search %s; '
                          'we need 1.7+, if any!' % (_vps_v,))
    # visaplan:
    from visaplan.plone.search.idxnames import getExcludeFromNav

# visaplan:
from visaplan.plone.tools.setup import make_reindexer, safe_context_id, step

# Logging / Debugging:
import logging

PROFILE_ID = 'visaplan.plone.animations:default'
CONTEXT_ID = safe_context_id(PROFILE_ID)
LOGGER_LABEL = CONTEXT_ID
logger = logging.getLogger(LOGGER_LABEL)


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'visaplan.plone.animations:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


@step
def reindex_animations_gcs(context, logger=logger):
    catalog = getToolByName(context, 'portal_catalog')
    # update_metadata: getThumbnailPath
    reindex = make_reindexer(catalog=catalog,
                             logger=logger,
                             update_metadata=True,
                             idxs=['getCustomSearch',
                                   'getCode',
                                   ])
    counter = Counter()
    for portal_type in [
            'FolderishAnimation',
	    ]:
        logger.info('Reindexing %(portal_type)r objects ...', locals())
        query = {
            'portal_type': portal_type,
            'Language': 'all',
            }
        for brain in catalog(query):
            if reindex(brain=brain):
                counter[portal_type] += 1
        num = counter[portal_type]
        logger.info('... %(num)d %(portal_type)r objects reindexed.',
                    locals())


@step
def reindex_animations_efs(context, logger=logger):
    catalog = getToolByName(context, 'portal_catalog')
    reindex = make_reindexer(catalog=catalog,
                             logger=logger,
                             idxs=[getExcludeFromNav,  # WIP: change index name
                                   ])
    counter = Counter()
    for portal_type in [
            'FolderishAnimation',
	    ]:
        logger.info('Reindexing %(portal_type)r objects ...', locals())
        query = {
            'portal_type': portal_type,
            'Language': 'all',
            }
        for brain in catalog(query):
            if reindex(brain=brain):
                counter[portal_type] += 1
        num = counter[portal_type]
        logger.info('... %(num)d %(portal_type)r objects reindexed.',
                    locals())

@step
def reload_gs_profile(context, logger=logger):
    loadMigrationProfile(
        context,
        CONTEXT_ID,
        )


