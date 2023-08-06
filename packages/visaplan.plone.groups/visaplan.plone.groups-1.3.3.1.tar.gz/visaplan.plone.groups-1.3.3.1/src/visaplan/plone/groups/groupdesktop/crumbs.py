# Python compatibility:
from __future__ import absolute_import

from importlib_metadata import PackageNotFoundError
from importlib_metadata import version as pkg_version

try:
    pkg_version('zope.deprecation')
except PackageNotFoundError:
    "Imports from old location not supported"
else:
    # Zope:
    from zope.deprecation import moved
    moved('visaplan.plone.groups.groupdesktop.oldcrumbs', 'version 1.4')
