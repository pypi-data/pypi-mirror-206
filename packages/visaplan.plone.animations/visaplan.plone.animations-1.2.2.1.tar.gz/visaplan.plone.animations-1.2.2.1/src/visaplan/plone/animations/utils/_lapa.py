"""
Helpers for the @@landing_path view (@@mainmenu version)

This is a simplified variant of the respective module in
visaplan.plone.structures; we don't care for structure elements here.
"""
# see (gf):
# ../../../../../../visaplan.plone.structures/src/visaplan/plone/structures/utils/_lapa.py
# ../../../../../../visaplan.plone.elearning/src/visaplan/plone/elearning/utils/_lapa.py

# Python compatibility:
from __future__ import absolute_import

from six.moves.urllib.parse import urlparse

try:
    # visaplan:
    from visaplan.plone.structures.utils import info_path
except ImportError:
    if __name__ != '__main__':
        raise

    def info_path(base, uid, crop=0):
        if not base.endswith('/'):
            base += '/'
        if crop:
            blist = base.split('/')
            del blist[-1-crop:-1]
            base = '/'.join(blist)
        return '%(base)s@@info?uid=%(uid)s' % locals()


__all__ = [
    'landingpath',
    ]


def landingpath(o, **kwargs):
    """
    Create a @@landing_path value

    Arguments:

      o -- the context object

    and, keyword-only:

      topic_path -- the matching @@mainmenu topic path

    If we found a @@mainmenu topic, we use this to hook our @@info view:

    >>> landingpath(MockObject('/know-how/virtual-construction-sites/a-site'),
    ...             topic_path='/construction-sites')
    ...                                       # doctest: +NORMALIZE_WHITESPACE
    '/construction-sites/@@info?uid=abc123'

    If we didn't find such @@mainmenu topic (e.g. because the object is not yet
    published and still located in the /temp/ folder, or the container is not
    covered by by any local search configuration), we use the containing parent
    directory instead:

    >>> landingpath(MockObject('/know-how/virtual-construction-sites/a-site'))
    ...                                       # doctest: +NORMALIZE_WHITESPACE
    '/know-how/virtual-construction-sites/@@info?uid=abc123'
    """
    pa = o.absolute_url_path()
    if pa == '/':
        return pa

    assert not pa.endswith('/')
    pop = kwargs.pop
    topic_path = pop('topic_path', None)

    uid = IUUID(o, None)
    if topic_path:
        return info_path(topic_path, uid)
    else:
        return info_path(pa, uid, crop=1)


# doctest support ...
class _Mock(object):
    def __init__(self, path):
        if path == '/':
            pass
        else:
            assert not path.endswith('/')
            if not path.startswith('/'):
                path = '/'+path
        self._path = path


class MockObject(_Mock):
    """
    >>> MockObject('some/path').absolute_url_path()
    '/some/path'
    """
    def absolute_url_path(self):
        return self._path


try:
    # Plone:
    from plone.uuid.interfaces import IUUID
except ImportError:
    if __name__ != '__main__':
        raise
    def IUUID(o, ignored):
        assert isinstance(o, MockObject)
        return 'abc123'


if __name__ == '__main__':
    # Standard library:
    import doctest
    doctest.testmod()
