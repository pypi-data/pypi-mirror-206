Changelog
=========


1.2.2.1 (2023-05-03)
--------------------

Bugfixes:

- When checking the version of the visaplan.plone.search package,
  compare correctly, following `PEP 440`_.

Requirements:

- packaging_

[tobiasherp]


1.2.2 (2023-05-02)
------------------

Improvements:

- As we use the traditional index `getExcludeFromNav`, we import the
  name of that index from visaplan.plone.search now, if available;
- The default is still ``getExcludeFromNav``.

Requirements:

- importlib_metadata_
- If we have visaplan.plone.search, we need 1.7+

Hints:

- The default value for the `getExcludeFromNav` index name
  will change in a future release.

[tobiasherp]


1.2.1 (2023-04-19)
------------------

Profile changes:

- Optional upgrade step to version 1005: refresh index `getExcludeFromNav`
  for FolderishAnimation objects.

  If you don't have that index (the *canonical* name is `exclude_from_nav` instead),
  just skip this step; an appropriate indexer is provided (but not activated) by
  visaplan.plone.search v1.6.2+.

Requirements:

- If visaplan.plone.search is installed, we need v1.6.2+,
  for a suitable `getExcludeFromNav` indexer.

[tobiasherp]


1.2.0 (2022-09-20)
------------------

New Features:

- getThumbnailPath for FolderishAnimations:
  .dx.FromImageAttribute with customized default thumbnail

Requirements:

- visaplan.plone.staticthumbnails v1.2.0

[tobiasherp]


1.1.3 (2022-03-04)
------------------

New Features:

- If visaplan.plone.structures is installed, the ``@@landing_path`` of
  FolderishAnimations points to the appropriate ``@@info`` path.
  Requires visaplan.plone.structures v1.2.7+.

Requirements:

- If visaplan.plone.menu is installed, we need v1.1.1+,
  for the ``@@mainmenu.current_topic_path`` method.

[tobiasherp]


1.1.2 (2021-11-17)
------------------

New Features:

- ``@@landing_path`` view for FolderishAnimation objects
  (no solution for target=_blank yet)

Requirements:

- If we have visaplan.plone.search, it must be v1.4.7+,
  providing the `ILandingPath` interface.

[tobiasherp]


1.1.1 (2021-09-07)
------------------

New Features:

- if visaplan.plone.industrialsector is installed, we'll have
  a ``code_formatted`` metadata column;
  with v1.1.2+, it should be created using the right language.

[tobiasherp]


1.1.0 (2021-06-30)
------------------

Bugfixes:

- Thumbnail generation works now, using visaplan.plone.staticthumbnails.mixin.dx.DedicatedThumbnailMixin
- Profile bugfix for ``Folder.xml``, ``allowed_content_types``:
  attribute `purge=False` was missing

Profile changes:

- Added behavior IDedicatedThumbnail
- Added upgrade step to reload the profile
- Increased profile version to 1004

Requirements:

- visaplan.plone.behaviors v1.1.0+
- visaplan.plone.staticthumbnails v1.1.0+

- Removed dependencies on

  - visaplan.plone.ajaxnavigation_
  - visaplan.tools_

[tobiasherp]


1.0.5 (2021-02-16)
------------------

New Features:

- `FolderishAnimation.getCustomSearch` method, providing (for now):

  - portal_type
  - Creator

Profile changes:

- Upgrade step to update the ``getCustomSearch`` indexes
- Profile version increased to 1002

[tobiasherp]


1.0.4 (2020-12-16)
------------------

Improvements:

- Made FolderishAnimations clickable even if lacking a preview image

[tobiasherp]


1.0.3 (2020-03-05)
------------------

- Views for AJAX navigation support (based on visaplan.plone.ajaxnavigation_)
- Added an ``ajax-nav`` view to prevent Plone from trying to load a FolderishAnimation via AJAX
  (since this doesn't work yet).
- Since it is not usable as an AJAX navigation target,
  the ``embed`` view has been renamed to ``onlyme``

[tobiasherp]


1.0.2 (2019-10-22)
------------------

- Removed *profile* dependency on visaplan.plone.behaviors, since the current version 1.0.2 doesn't have one.

[tobiasherp]


1.0.1 (2019-06-26)
------------------

- Support for preloader images, recognized by name
- use visaplan.plone.staticthumbnails_
- Add CSS classes to HTML text

[tobiasherp]


1.0 (2019-05-20)
----------------

- Initial release.
  [tobiasherp]

.. _importlib_metadata: https://pypi.org/project/importlib-metadata/
.. _packaging: https://pypi.org/project/packaging/
.. _`PEP 440`: https://peps.python.org/pep-0440/
.. _visaplan.plone.ajaxnavigation: https://pypi.org/project/visaplan.plone.ajaxnavigation
.. _visaplan.plone.staticthumbnails: https://pypi.org/project/visaplan.plone.staticthumbnails
.. _visaplan.tools: https://pypi.org/project/visaplan.tools
