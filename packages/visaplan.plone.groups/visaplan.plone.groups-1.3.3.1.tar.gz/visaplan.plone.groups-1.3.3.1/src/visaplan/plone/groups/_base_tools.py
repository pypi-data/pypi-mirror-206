"""
visaplan.plone.groups._base_tools: tools for the .base module
"""

# Python compatibility:
from __future__ import absolute_import

# visaplan:
from visaplan.tools.coding import safe_decode


def _add_nonempty_list(key, label, dolists, lodicts, sortkey=None):
    """
    Little helper for .base.my_groups(grouped=1)

    Arguments:
      key -- a key in the `dolists` dict of lists
      label - the 'label' value for the dict to be appended to the list of
              dicts
      dolists - the dict of lists (input data)
      lodicts - the list of dicts, for use as optgroups (output data)
      sortkey - a function to be used as the sort() or sorted() key option

    >>> f = _add_nonempty_list
    >>> dic = {'managed': [], 'desktop': ['group_a', 'group_B']}
    >>> res = []
    >>> kw={'dolists': dic, 'lodicts': res,
    ...     'sortkey': lambda x: x.lower()}
    >>> f('managed', 'Groups managed by me', **kw)
    >>> res
    []
    >>> list(dic.keys())
    ['desktop']
    >>> f('desktop', 'Groups with desktop enabled', **kw)
    >>> res                                    # doctest: +NORMALIZE_WHITESPACE
    [{'items': ['group_a', 'group_B'],
      'key': 'desktop', 'label': 'Groups with desktop enabled'}]
    >>> not dic
    True
    """
    thelist = dolists.pop(key, None)
    if not thelist:
        return
    thelist.sort(key=sortkey)
    lodicts.append({
        'label': label,
        'items': thelist,
        'key':   key,
        })


def groups_sortkey(dic):
    """
    Return a sort[ed] key for groupinfo dictionaries.

    >>> k = groups_sortkey

    Input values are dictionaries; dicts without a 'title' key are considered
    garbabe:
    >>> k({'id': 'some_group'})
    (99, u'garbage last')

    However, dicts which describe real groups are much more interesting:
    >>> k({'group_title': 'Some Interesting Course learner'})
    ...                                        # doctest: +NORMALIZE_WHITESPACE
    (0, u'some interesting course learner',
        u'Some Interesting Course learner')

    If the title is empty, we'll get:
    >>> k({'group_id': 'GROUP_WITHOUT_TITLE'})
    (1, u'group_without_title', u'GROUP_WITHOUT_TITLE')

    ... which will cause any untitled groups to be sorted last:
    >>> liz = [{'group_title': 'some interesting course learner'},
    ...        {'group_id': 'group_Without_Title'},
    ...        {'bugus': 'piece of junk'},
    ...        {'group_title': 'some less interesting course Author'}]
    >>> sorted(liz, key=k)                     # doctest: +NORMALIZE_WHITESPACE
    [{'group_title': 'some interesting course learner'},
     {'group_title': 'some less interesting course Author'},
     {'group_id': 'group_Without_Title'},
     {'bugus': 'piece of junk'}]
    """
    s = dic.get('group_title')
    untitled = int(not s)
    if untitled:
        s = dic.get('group_id')
        if not s:
            return (99, u'garbage last')
    s = safe_decode(s)
    low = s.strip().lower()
    return (untitled, low, s)


if __name__ == '__main__':
    # Standard library:
    from doctest import testmod
    testmod()
