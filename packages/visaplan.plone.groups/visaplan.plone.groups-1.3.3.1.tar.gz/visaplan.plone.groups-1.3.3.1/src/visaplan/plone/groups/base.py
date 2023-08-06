# -*- coding: utf-8 -*- Umlaute: ÄÖÜäöüß
"""
visaplan.plone.groups: base
"""

# Python compatibility:
from __future__ import absolute_import, print_function

# Standard library:
from collections import defaultdict

# Zope:
from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from zope.component import getMultiAdapter

# visaplan:
from visaplan.plone.infohubs.hubs2 import context_and_form_tuple
from visaplan.plone.tools.context import make_translator
from visaplan.plone.tools.groups import (
    build_groups_set,
    get_all_members,
    groupinfo_factory,
    is_direct_member__factory,
    is_member_of__factory,
    is_member_of_any,
    userinfo_factory,
    )
from visaplan.tools.classes import Proxy
from visaplan.tools.coding import safe_decode
from visaplan.tools.dates import make_date_formatter
from visaplan.tools.lands0 import list_of_strings
from visaplan.tools.profile import StopWatch

# Local imports:
from ._base_pio import _po_my_groups
from ._base_tools import _add_nonempty_list, groups_sortkey
from .groupsharing.utils import (
    datefromform,
    default_dates_dict,
    getcoursetitle,
    getgrouptitle,
    gettitle,
    journal_text,
    make_break_at_row,
    make_keyfunction,
    makedate,
    )
from visaplan.plone.groups.infofact import (
    get_group_mapping_course__factory,
    memberinfo_factory,
    )
from visaplan.plone.groups.unitraccgroups.utils import (
    ALL_GROUP_SUFFIXES,
    ALUMNI_SUFFIX,
    LEARNER_SUFFIX,
    pretty_group_title,
    split_group_id,
    )

# Logging / Debugging:
from visaplan.plone.tools.log import getLogSupport

logger, debug_active, DEBUG = getLogSupport()

BORING_GROUPS = set(['AuthenticatedUsers'])
sw_kwargs = {'enable': bool(debug_active),
             }


class GroupsBase(BrowserView):
    """
    Provide base functionality for the browser views:

    - groupboard/browser.py
    """

    def desktop_groups(self, desktop=1, **kwargs):
        """
        Return a list of desktop-enabled groups the current user is a member of
        """
        return self.my_groups(desktop=desktop, **kwargs)

    def admin_or_desktop_groups(self, desktop=1, managed=1, grouped=1,
                                **kwargs):
        """
        Like desktop_groups, but include administrated groups as well.

        This includes not *all* groups the current user may manage
        (if having global group administration permission)
        but only those (s)he is configured to be group_manager.
        """
        return self.my_groups(desktop=desktop, managed=managed, grouped=grouped,
                              **kwargs)

    def my_groups(self, **kw):
        """
        Return a list of groups the current user is a member of.

        With grouped=0, returns a list of groupinfo dictionaries;
        with grouped=1, returns a list of optgroup dictionaries
        (keys 'label' and 'items').

        For default values and other keyword options,
        see the _po_my_groups function.

        NOTE:
        This function doesn't filter the groups as smartly as the old
        @@groupsharing.get_courses_and_desktop_groups method (yet);
        however, we are not interested in the courses on the desktop anymore,
        and removal of this functionality is in progress.

        See the .my_groups_old method benlow.
        """
        user = self.get_loggedin_user()
        all_ids = [N for N in user.getGroups() if N != 'AuthenticatedUsers']
        if not all_ids:
            return []

        kwargs = {}
        kwargs.update(kw)
        _po_my_groups(kwargs)
        context = self.context  # b 91 (includeany)
        gi = groupinfo_factory(context, pretty=1, missing=1)
        # the groupinfo won't provide the group properties (yet):
        desktop = kwargs['desktop']
        managed = kwargs['managed']
        grouped = kwargs['grouped']
        other = kwargs['other']

        # if ignoring the desktop flag, we effectively ignore other flags as
        # well; so, if not grouping, we can keep it simple:
        includeany = other or desktop == 'ignore'
        if includeany and not grouped:
            res = [gi(theid) for theid in all_ids]
            res.sort(key=groups_sortkey)
            return res

        if managed:
            my_id = user.getId()

        bucket = {
            'desktop': 'desktop',
            'managed': 'managed',
            'other':   'other',
            }
        if not grouped:
            for key in bucket.keys():
                bucket[key] = 'any'
        lists = {}
        for key in set(bucket.values()):
            lists[key] = []
        if desktop == 'ignore':
            other = True

        pg = getToolByName(context, 'portal_groups')
        get_group = pg.getGroupById
        key = None
        for theid in all_ids:
            dic = gi(theid)
            if not dic['exists']:
                # TODO: bucket['missing'] and/or 'disabled' keys
                continue
            go = get_group(theid)
            # if not go: continue
            getprop = go.getProperty
            if managed:
                prop = getprop('group_manager')
                if prop == my_id:
                    key = bucket['managed']
            if key is None and desktop:
                prop = getprop('group_desktop')
                if prop:
                    key = bucket['desktop']
            if key is None and other:
                key = bucket['other']
            if key is None:
                continue
            # lists[key].append(gi(theid))
            lists[key].append(dic)
            key = None

        if not grouped:
            res = lists['any']
            res.sort(key=groups_sortkey)
            return res

        res = []

        alkw = {
            'dolists': lists,   # dict of lists (input)
            'lodicts': res,     # list of dicts (output)
            'sortkey': groups_sortkey, # for sort[ed] built-in resp. method
            }
        _add_nonempty_list('managed', ""'Groups managed by me', **alkw)
        _add_nonempty_list('desktop', ""'Desktop-enabled groups', **alkw)
        _add_nonempty_list('other',   ""'Other groups' if res
                                      else ""'Selectable groups',
                                      **alkw)
        assert not lists, ('unexpected / forgotten key(s) to list(s): %s' % (
            list(lists.keys()),
            ))

        return res

    def current_group_id(self):
        """
        Return the currently "active" (specified) group id.

        Oh well.
        We usually use the 'gid' request variable, but we have a 'group' option
        to the groupboard/new-thread.pt template as well.
        """
        gid = self.request.get('gid')
        if gid == 'None' or not gid:
            return None
        return gid

    def get_loggedin_user(self):
        """
        Return the authenticated user, or raise Unauthorized
        """
        context = self.context
        pm = getToolByName(context, 'portal_membership')
        if pm.isAnonymousUser():
            raise Unauthorized
        return pm.getAuthenticatedMember()

    def can_access_group(self, gid):
        """
        Is the current user allowed to access the given group?
        """
        user = self.get_loggedin_user()
        groups = user.getGroups()  # a list
        if gid not in groups:
            return 0
        # we might add more (optional) constraints, e.g. the group_desktop
        # to be enabled, or perhaps the user to be the configured group_manager.
        # For now, all members may write.
        return 1

    # --------------------------------------------- [ my_groups_old() ... [
    # see as well:
    #     .my_groups()                                  (above)
    #
    # and in @@groupsharing, ./groupsharing/browser.py:
    #     .voc_get_explicit_group_memberships_for_auth()
    #     .get_groups_by_user_id()
    #     .get_all_group_ids()
    #     ._get_all_group_ids()
    #     .get_all_groups_including_user()
    #     .get_all_groups()
    #     ._get_filtered_groups()
    #     .get_user_and_all_groups()
    #     .get_group_memberships
    #     .get_manageable_groups
    #     .get_group_info_by_id
    # ... (oh my!)
    # and ...
    #      _ids

    def my_groups_old(self, user_id=None, direct_only=1, grouped=0):
        """
        Use the old get_courses_and_desktop_groups() functionality to the
        selectable groups.

        Be prepared for this method to be removed,
        once the new .my_groups method (above) is able to satisfy the needs.
        """
        if user_id is None:
            user = self.get_loggedin_user()
            user_id = user.getId()
        return self._get_courses_and_desktop_groups(user_id,
            direct_only=direct_only, grouped=grouped)[1]

    def _get_courses_and_desktop_groups(self, user_id, gid=None,  # (gcadg)
                                        direct_only=1, grouped=0):
        """
        A copy of the @@groupsharing version of the
        get_courses_and_desktop_groups method; we'll try to remove any
        expensive courses functionality here ...

        Gib zwei Listen zurück (courses, desktops1):
        - die Kurse mit den schreibtischrelevanten Gruppen
        - die Gruppen, für die Schreibtische existieren
        """  # ----------------------------------------- [ gcadg ... [
        context = self.context
        getAdapter = context.getAdapter
        with StopWatch('@@gd.gcadg', **sw_kwargs) as stopwatch:
            is_direct_member_of = is_direct_member__factory(context, user_id)
            # Verwendung der Gruppeninfo sowohl für Kurse als auch für
            # Schreibtische; teure Berechnung puffern:
            group_info = Proxy(groupinfo_factory(context,
                                                 pretty=1,
                                                 forlist=0))

            courses = []
            alumni_gids = []  # Alumni-Gruppen
            desktops1 = []  # 'desktop'
            acl = getToolByName(context, 'acl_users')
            user = acl.getUser(user_id)
            if not user:
                return courses, desktops1

            include_other = not direct_only
            desktops2 = []  # 'managed'
            desktops3 = []  # 'other'
            all_groups_of_user = set(user.getGroups())
            get_mapping_group = get_group_mapping_course__factory(
                    context,
                    group_ids=all_groups_of_user,
                    group_info=group_info)
            stopwatch.lap('Vorbereitungen')
            # ------------------- [ gcadg: Kursgruppen ... [
            if gid is None:
                # persönlicher Schreibtisch - Kursgruppen ungefiltert
                for group_id in all_groups_of_user:
                    if group_id in BORING_GROUPS:
                        continue
                    # dic wird auch für ungefilterte Kurse verwendet:
                    dic = group_info[group_id]
                    if is_direct_member_of(group_id):
                        if dic['group_desktop']:
                            desktops1.append(dic)
                        elif dic['group_manager'] == user_id:
                            desktops2.append(dic)
                        elif group_id == gid:
                            desktops3.append(dic)
                    elif include_other:
                        if dic['group_manager'] == user_id:
                            desktops2.append(dic)
                        elif dic['group_desktop']:
                            desktops3.append(dic)
                    role = dic.get('role')
                    if role == LEARNER_SUFFIX:
                        courses.append(get_mapping_group(group_id))
                    elif role == ALUMNI_SUFFIX:
                        alumni_gids.append(group_id)
                stopwatch.lap('Alle Kurse des Users')

                # unbesuchte und ungebuchte, aber zugängliche Gruppen:
                portal_catalog = getToolByName(context, 'portal_catalog')
                portal_state = getMultiAdapter((context, self.request),
                                               name=u'plone_portal_state')
                found_uids = set([dic['course_uid'] for dic in courses])
                for rs in ('visible', 'published'):
                    query = {
                        'portal_type': 'UnitraccCourse',
                        'review_state': rs,
                        'sort_on': 'effective',
                        'sort_order': 'descending',
                        }
                    for brain in portal_catalog(query):
                        uid = brain.UID
                        if uid in found_uids:
                            continue
                        courses.append({
                            'course_brain': brain,
                            'course_title': brain.Title,
                            'course_uid': uid,
                            'currently_booked': False,
                            'stats': None,
                            'id': None,
                            })
                stopwatch.lap('Ungebuchte Kurse')

            else:
                # Gruppenschreibtisch - nur Kurse über die aktuelle Gruppe
                for group_id in all_groups_of_user:
                    if group_id in BORING_GROUPS:
                        continue
                    if is_direct_member_of(group_id):
                        dic = group_info[group_id]
                        if dic['group_desktop']:
                            desktops1.append(dic)
                        elif dic['group_manager'] == user_id:
                            desktops2.append(dic)
                        elif group_id == gid:
                            desktops3.append(dic)

                pg = getToolByName(context, 'portal_groups')
                group = pg.getGroupById(gid)
                if group:
                    all_groups_of_group = set(group.getGroups())
                else:
                    all_groups_of_group = set()

                for group_id in all_groups_of_group:
                    if group_id in BORING_GROUPS:
                        continue
                    dic = group_info[group_id]
                    role = dic.get('role')
                    if role == LEARNER_SUFFIX:
                        courses.append(get_mapping_group(group_id))
                    elif role == ALUMNI_SUFFIX:
                        alumni_gids.append(group_id)
                stopwatch.lap('Nur Kurse der Gruppe')

            alumni_uids = set([get_mapping_group(gid)['course_uid']
                               for gid in alumni_gids
                               ])
            # ------------------- ] ... gcadg: Kursgruppen ]

            if debug_active:
                pp(courses=courses, alumni_gids=alumni_gids,
                   alumni_uids=sorted(alumni_uids))
            course_uids = set()
            if courses:
                # wenn Kurse gefunden, Statistiken ermitteln
                for dic in courses:
                    uid = dic.get('course_uid')
                    if uid is not None:
                        course_uids.add(uid)
                # Statistiken sind mit Autoren-UID verknüpft:
                author = context.getBrowser('author').get()
                if author:
                    author_uid = author.UID()
                    query_data = {'user_uid': author_uid,
                                  'course_uid': sorted(course_uids),
                                  }
                    stat_dict = {}
                    with getAdapter('sqlwrapper') as sql:
                        rows = sql.select('course_statistics_overview',
                                          query_data=query_data)
                        for row in rows:
                            course_uid = row['course_uid']
                            stat_dict[course_uid] = row
                    for dic in courses:
                        course_uid = dic['course_uid']
                        dic['stats'] = stat_dict.get(course_uid)
                        dic['coursedocs_link'] = course_uid in alumni_uids
                        dic['currently_booked'] = True
                stopwatch.lap('Kursstatistiken')

            alumni_uids.difference_update(course_uids)
            if alumni_uids:
                # abgelaufene Kursgruppen: separat auflisten
                alumnig = []
                for uid in alumni_uids:
                    dic = get_mapping_group(''.join(('group_', uid, '_', ALUMNI_SUFFIX)))
                    dic['coursedocs_link'] = True
                    dic['currently_booked'] = False
                    alumnig.append(dic)
                if alumnig[1:]:
                    alumnig.sort(key=getcoursetitle)
                courses.extend(alumnig)

            if grouped:
                groups = []
                if desktops2:
                    desktops2.sort(key=getgrouptitle)
                    groups.append({
                        'key': 'managed',
                        'label': ""'Groups managed by me',
                        'items': desktops2,
                        })
                if desktops1:
                    desktops1.sort(key=getgrouptitle)
                    groups.append({
                        'key': 'desktop',
                        'label': ""'Desktop-enabled groups',
                        'items': desktops1,
                        })
                if desktops3:
                    desktops3.sort(key=getgrouptitle)
                    groups.append({
                        'key': 'other',
                        'label': ""'Other groups' if groups
                                 else ""'Selectable groups',
                        'items': desktops3,
                        })
            else:
                desktops1.sort(key=getgrouptitle)  # Gruppen mit Schreibtisch
                desktops2.sort(key=getgrouptitle)  # von mir administrierte Gruppen
                # bestimmte Gruppen ohne Schreibtisch
                # trotzdem anhängen - aber als letztes:
                desktops1.extend(desktops2)
                groups = desktops1
            return courses, groups  # --------------- ] ... gcadg ]
    # --------------------------------------------- ] ... my_groups_old() ]
