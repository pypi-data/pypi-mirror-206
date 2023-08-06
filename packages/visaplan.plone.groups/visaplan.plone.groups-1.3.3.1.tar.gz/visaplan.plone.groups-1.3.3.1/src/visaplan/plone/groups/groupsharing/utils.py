# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=79
"""
utils.Modul für Browser groupsharing

Autor: Tobias Herp
"""
# Python compatibility:
from __future__ import absolute_import, print_function

from six import iteritems as six_iteritems
from six import string_types as six_string_types
from six.moves import map

# Standard library:
from collections import defaultdict
from datetime import date
from time import strftime

# visaplan:
from visaplan.plone.tools.groups import build_groups_set
from visaplan.tools.coding import safe_decode


def makedate(s, default=None):
    """
    Konvertiere ein Datum aus einem Datepicker-Datumsfeld

    >>> import datetime
    >>> makedate('1.4.2014')
    datetime.date(2014, 4, 1)

    Siehe auch unitracc.tools.forms.make_date_parser
    (ohne default-Wert, mit strptime)
    """
    if not s:
        return default
    if isinstance(s, six_string_types):
        liz = list(map(int, s.split('.')))
    else:
        liz = list(map(int, s))
    assert len(liz) == 3, '"d.m.yyyy" date value expected (%r)' % s
    liz.reverse()
    return date(*tuple(liz))


def datefromform(prefix, name, form, default=None, logger=None):
    """
    Lies einen Datumswert aus den Formulardaten, unter Tolerierung
    fehlerhafter Formulardaten (wenn reparierbar)

    >>> form={'start_heinz': '2016-05-02',
    ...       'end_heinz': ('', ''),
    ...       'end_nemo': ('', '2016-06-17')}
    >>> datefromform('start_', 'heinz', form)
    datetime.date(2016, 5, 2)
    >>> datefromform('end_', 'heinz', form)
    >>> datefromform('end_', 'nemo', form)
    Traceback (most recent call last):
      ...
    ValueError: Single value expected; 2-tuple of identical values tolerated

    """
    key = prefix + name
    val = form.get(key, default)
    if val is None:
        return val
    result = None
    try:
        result = makedate(val, default)
    except ValueError as e:
        if logger is not None:
            logger.error('Value for %(key)r: invalid date (%(val)r)', locals())
        if isinstance(val, (list, tuple)):
            if len(val) == 2 and val[0] == val[1]:
                result = makedate(val[0], default)
            else:
                logger.error("Can't recover from error!")
                logger.exception(e)
                raise
        else:
            raise
    finally:
        return result


def default_dates_dict():
    """
    zur Verwendung mit defaultdict
    """
    return {'start_date': None,
            'end_date': None,
            }


def build_groups_depthdict(dic, userid):
    """
    Erzeugt ein dict, das die Gruppen-IDs und die Rekursionstiefen enthält.

    >>> dic = {'group_a': ['group_b', 'group_c'],
    ...        'group_b': ['user_a', 'user_b'],
    ...        'group_c': ['user_c'],
    ...        }
    >>> groups = build_groups_depthdict(dic, 'user_a')
    >>> groups['user_a']
    0
    >>> groups['group_b']
    1
    >>> groups['group_a']
    2
    >>> sorted(groups.items())
    [('group_a', 2), ('group_b', 1), ('user_a', 0)]
    """
    groups_dict = {userid: 0}  # Identität
    groups = set([userid])
    # ------------------------------ [ after _traverse_dict ... [
    # (a helper for visaplan.plone.tools.groups.build_groups_set)
    iterations = 1
    newly_found = set()
    while True:
        for gid, members in six_iteritems(dic):
            if gid in groups:
                continue
            if groups.intersection(members):
                newly_found.add(gid)
        if newly_found:
            groups.update(newly_found)
            while newly_found:
                gid = newly_found.pop()
                groups_dict[gid] = iterations
            iterations += 1
        else:
            break
    # ------------------------------ ] ... after _traverse_dict ]
    return groups_dict


def build_groups_reversedict(dic):
    """
    Erzeuge ein dict-Objekt, das die Zuordnungen umkehrt:

    >>> dic = {'group_a': ['group_b', 'group_c'],
    ...        'group_b': ['user_a', 'user_b'],
    ...        'group_c': ['user_c'],
    ...        }
    >>> membership = build_groups_reversedict(dic)
    >>> membership['user_a']
    set(['group_b'])
    >>> sorted(membership.items())
    [('group_b', set(['group_a'])), ('group_c', set(['group_a'])), ('user_a', set(['group_b'])), ('user_b', set(['group_b'])), ('user_c', set(['group_c']))]

    Das Ergebnis-dict enthält nur die direkten Zuordnungen;
    die rekursive Auflösung ist ein weiterer Schritt.
    """
    revdic = defaultdict(set)
    for gid, members in dic.items():
        for uog in members:
            revdic[uog].add(gid)
    return dict(revdic)


def recursive_memberships(uogid, revdic, exclude_member=False):
    """
    Ermittle die rekursiv aufgelösten Gruppenmitgliedschaften des übergebenen
    Users bzw. der Gruppe (uogid, "user or group id") anhand des revertierten
    dicts (erzeugt von --> build_groups_reversedict)

    >>> dic = {'group_a': ['group_b', 'group_c'],
    ...        'group_b': ['user_a', 'user_b'],
    ...        'group_c': ['user_c'],
    ...        }
    >>> membership = build_groups_reversedict(dic)
    >>> gm = recursive_memberships('user_a', membership)
    >>> sorted(gm)
    ['group_a', 'group_b', 'user_a']

    Das "anfragende Mitglied" ist im Ergebnis enthalten;
    für User-IDs macht es Sinn, exclude_member=True zu übergeben:
    >>> sorted(recursive_memberships('user_a', membership, True))
    ['group_a', 'group_b']

    Zirkelschlüsse sind unkritisch; sie führen lediglich dazu, daß die
    angefragte Gruppe in der zurückgegebenen Menge enthalten ist:
    >>> dic.update({'group_d': ['group_e'],
    ...             'group_e': ['group_f'],
    ...             'group_f': ['group_d'],
    ...             'group_A': ['group_B'],
    ...             'group_B': ['group_A'],
    ...             })
    >>> membership = build_groups_reversedict(dic)
    >>> sorted(recursive_memberships('group_d', membership))
    ['group_d', 'group_e', 'group_f']
    >>> sorted(recursive_memberships('group_A', membership))
    ['group_A', 'group_B']

    User, die in keiner Gruppe sind:
    >>> recursive_memberships('user_x', membership, True)
    set([])
    """
    res = set([uogid])
    try:
        newly_found = set(revdic[uogid])
    except KeyError:  # User ohne Gruppe
        pass
    else:
        while newly_found:
            res.update(newly_found)
            this_iteration = set()
            for gid in newly_found:
                try:
                    found_here = revdic[gid].difference(res)
                    if found_here:
                        this_iteration.update(found_here)
                except KeyError:
                    pass
            res.update(this_iteration)
            newly_found = this_iteration
    finally:
        if exclude_member:
            res.discard(uogid)
        return res


# ------------------------- [ Funktionen zum Sortieren ... [
def make_keyfunction(key, factory=None):
    """
    Factory-Funktion: gib eine Funktion zurück, die als Schlüsselfunktion
    verwendet werden kann (list.sort(key=make_keyfunction(...)).

    >>> dic={'id': 123, 'title': 'Alphanumeric'}
    >>> make_keyfunction('id')(dic)
    123
    >>> make_keyfunction('title')(dic)
    'Alphanumeric'

    Verwendung zum Sortieren:

    >>> dic2={'id': 456, 'title': 'Aaa'}
    >>> dic3={'id': 100, 'title': 'bbb'}
    >>> liz=[dic, dic2, dic3]
    >>> sorted(liz, key=make_keyfunction('id'))
    [{'id': 100, 'title': 'bbb'}, {'id': 123, 'title': 'Alphanumeric'}, {'id': 456, 'title': 'Aaa'}]
    >>> sorted(liz, key=make_keyfunction('title'))
    [{'id': 456, 'title': 'Aaa'}, {'id': 123, 'title': 'Alphanumeric'}, {'id': 100, 'title': 'bbb'}]

    Das optionale Argument <factory> ist eine Funktion, die den Wert für die
    Rückgabe transformiert (z. B. für Zahlen, die als Strings abgespeichert
    sind).
    """
    if factory is None:
        def keyfunc(dic):
            return dic[key]
    else:
        def keyfunc(dic):
            return factory(dic[key])
    return keyfunc


# schonmal vorgefertigt:
def getgrouptitle(dic):
    """
    Oft benötigte Schlüsselfunktion zum Sortieren von Listen von Dictionarys
    """
    return safe_decode(dic.get('group_title', ''))


def getcoursetitle(dic):
    """
    Schlüsselfunktion für Ergebnisse von
    .browser.get_group_mapping_course__factory()()
    """
    return safe_decode(dic.get('course_title', ''))


def gettitle(dic):
    """
    Dasselbe wie:
    gettitle = make_keyfunction('title', safe_decode)

    >>> dic={'id': 'abc123', 'title': 'Alphanumeric'}
    >>> gettitle(dic)
    u'Alphanumeric'
    >>> make_keyfunction('title')(dic)
    'Alphanumeric'
    """
    return safe_decode(dic.get('title', ''))
# ------------------------- ] ... Funktionen zum Sortieren ]


# ------------------------- [ Funktionen für Debugging ... [
def make_break_at_row(member_id):
    """
    Als Kriteriuzm für bedingten Breakpoint; Beispiel:

      break_at_row = make_break_at_row('Enrico')
      b 123, break_at_row(row)
    """
    # Standard library:
    from pprint import pprint
    break_all = None
    break_none = False
    if isinstance(member_id, six_string_types):
        member_ids = set([member_id])
    elif isinstance(member_id, (bool, int)):
        break_all = bool(member_id)
    elif member_id is None:
        break_none = True
    else:
        member_ids = set(member_id)

    def break_at_row(row):
        pprint(('row:', row))
        if break_all is not None:
            return break_all
        elif break_none:
            return False
        else:
            try:
                return row['member_id_'] in member_ids
            except KeyError as e:
                print(e)
                print('Schluessel fehlt!')
                return True
    return break_at_row


def journal_text(lst):
    res = []
    for tup in lst:
        ok, txt = tup
        res.append('%s: %s' %
                   (ok and 'OK' or 'Fehler',
                    txt))
    # res.append('')
    return '\n'.join(res)
# ------------------------- ] ... Funktionen für Debugging ]


if __name__ == '__main__':
    # Standard library:
    import doctest
    doctest.testmod()
