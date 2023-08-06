"""
visaplan.plone.group._base_pio: parse init options

This module provides functions to parse options to more complex functions or
methods, separated out for testability.
"""

# Python compatibility:
from __future__ import absolute_import


def _po_my_groups(kwdict):
    """
    Parse options for the .base.GroupsBase.my_groups method

    The given dict is modified in-place; we need a dict to see the effect:
    >>> kw = {'desktop': 1}
    >>> po = _po_my_groups
    >>> po(kw)
    >>> sorted(kw.items())  # +DOCTEST_NORMALIZE_WHITESPACE
    [('desktop', 1), ('grouped', 0), ('managed', 0), ('other', 0)]

    We'll create a little test helper:
    >>> def tst(**kw):
    ...     _po_my_groups(kw)
    ...     return sorted(kw.items())

    So, the default is currently to ignore the desktop flag:
    >>> tst()
    [('desktop', 'ignore'), ('grouped', 0), ('managed', 0), ('other', 0)]

    With other groups of groups activated, we imply grouping:
    >>> tst(managed=1)
    [('desktop', 1), ('grouped', 1), ('managed', 1), ('other', 0)]
    >>> tst(managed=1, desktop=1)
    [('desktop', 1), ('grouped', 1), ('managed', 1), ('other', 0)]

    To be more precise: this is because we have more than one category of
    groups queried.
    If asking e.g. for managed groups only, we don't default to grouping:

    >>> tst(managed=1, desktop=0)
    [('desktop', 0), ('grouped', 0), ('managed', 1), ('other', 0)]

    We'll refuse silly queries:
    >>> tst(desktop=0)
    Traceback (most recent call last):
      ...
    ValueError: Your choice of groups filters doesn't make sense!

    And we refuse unsupported named options, of course:
    >>> tst(silly=1)
    Traceback (most recent call last):
      ...
    TypeError: Illegal / unsupported option(s): ('silly',)

    """
    setdef = kwdict.setdefault
    allowed = set(['desktop', 'grouped', 'managed', 'other'])
    forbidden = set(kwdict) - allowed
    if forbidden:
        forbidden = tuple(sorted(forbidden))
        raise TypeError('Illegal / unsupported option(s): %(forbidden)s'
                        % locals())

    managed = setdef('managed', 0)
    other   = setdef('other', 0)
    desktop = setdef('desktop', 1 if managed or other
                                  else 'ignore')
    choices = len([_f for _f in [desktop, managed, other] if _f])
    if choices > 1:
        grouped = setdef('grouped', 1)
    elif choices == 1:
        grouped = setdef('grouped', 0)
    else:
        raise ValueError('Your choice of groups filters doesn\'t make sense!')


if __name__ == '__main__':
    # Standard library:
    from doctest import testmod
    testmod()

