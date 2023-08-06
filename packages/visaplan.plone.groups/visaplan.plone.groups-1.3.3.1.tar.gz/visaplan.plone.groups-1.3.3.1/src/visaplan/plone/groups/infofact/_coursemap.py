# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et hls tw=79
# visaplan.plone.groups:infofact: map courses to groups;
# related to visaplan.plone.elearning

# Python compatibility:
from __future__ import absolute_import

# Zope:
from Products.CMFCore.utils import getToolByName

# visaplan:
from visaplan.plone.tools.context import getbrain

__all__ = [
    'get_group_mapping_course__factory',
    ]


def get_group_mapping_course__factory(context, group_ids, group_info):
    """
    "get (the) group mapping (the) course"

    Erzeuge eine Funktion, die die Gruppe zurückgibt, die
    - die übergebene Kursgruppe vermittelt, und
    - einen Schreibtisch erzeugt

    Argumente:
    group_ids - vorab ermittelte Menge aller interessierenden Gruppen
                (in denen der Benutzer direkt oder indirekt Mitglied ist)
    group_info - ein dict-Objekt zur Pufferung aller angeforderten
                 Gruppen-Infos (siehe visaplan.tools.classes.Proxy)
    """
    acl = getToolByName(context, 'acl_users')
    gpm = acl.source_groups._group_principal_map

    def get_group_mapping_course(coursegroup_id):
        """
        Gib die erste Gruppe zurück, die die übergebene Kursgruppe vermittelt

        coursegroup_id - die ID einer primären Kursgruppe, die evtl. einen
                         Schreibtisch erzeugt, wahrscheinlich aber nicht

        Das Ergebnis enthält:
        - garantiert den Schlüssel 'coursegroup_id'
        - einen Schlüssel 'stats' für die (hier nicht gefüllte!) Statistik
        - UID, Title und Brain des Kurses
        - im Erfolgsfall die Gruppeninfo der nächsten vermittelnden Gruppe
          (bei user_id -> group_a -> group_b -> group_abc123_learner wäre das
          die der Gruppe group_a)
        """
        course_uid, pseudorole = coursegroup_id.split('_')[1:]
        course_brain = getbrain(context, course_uid)
        dic2 = {'coursegroup_id': coursegroup_id,
                'course_uid': course_uid,
                'course_brain': course_brain,
                'course_title': course_brain and course_brain.Title,
                'stats': None,
                }
        done = set()

        def inner(group_id):
            if group_id in done:
                return
            done.add(group_id)
            if group_id not in group_ids:
                return
            # zuerst die Rekursion:
            for child_id in gpm[group_id]:
                res = inner(child_id)
                if res is not None:
                    return res
            try:
                dic = group_info[group_id]
                if dic['group_desktop']:
                    return dic
            except KeyError:
                pass

        dic = inner(coursegroup_id)
        if dic is not None:
            dic2.update(dic)
        return dic2

    return get_group_mapping_course
