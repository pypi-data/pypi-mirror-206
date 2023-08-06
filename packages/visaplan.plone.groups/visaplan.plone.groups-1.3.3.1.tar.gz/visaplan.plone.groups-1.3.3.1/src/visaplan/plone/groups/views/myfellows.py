# Python compatibility:
from __future__ import absolute_import

# Zope:
from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements

# visaplan:
from visaplan.plone.base.permissions import ACCESS_DESKTOP
from visaplan.plone.browsers.author.utils import (
    get_title_and_name,
    joinNonemptyAttributes,
    )
from visaplan.plone.infohubs import make_hubs
from visaplan.plone.tools.context import make_translator
from visaplan.plone.tools.groups import groupinfo_factory

# Logging / Debugging:
from visaplan.plone.tools.log import getLogSupport

logger, debug_active, DEBUG = getLogSupport()

# Local imports:
from .._idxnames import getExcludeFromNav
from ..base import GroupsBase
from ..interfaces import IMyFellows

REQUIRE_DESKTOP_FLAG = 0


class MyFellows(GroupsBase):
    implements(IMyFellows)

    def data(self):
        """
        Provide data for ./myfellows.pt
        """
        gid = self.current_group_id()
        ## may raise Unauthorized:
        #optgroups = self.desktop_groups(other=1, grouped=1)
        user = self.get_loggedin_user()
        user_id = user.getId()
        optgroups = self.my_groups_old(user_id, grouped=1)

        context = self.context
        hub, info = make_hubs(context)
        _ = make_translator(context)
        errors = []

        members = None
        group_manager = None
        groupdict = None
        refered = None
        if gid:
            gi = groupinfo_factory(context, pretty=1, missing=1)
            groupdict = gi(gid)
            if not groupdict['exists']:
                errors.append(_("Won't list members of non-existing group!"))
            elif not REQUIRE_DESKTOP_FLAG or gid in whitelist:
                pg = getToolByName(context, 'portal_groups')
                get_group = pg.getGroupById
                go = get_group(gid)
                if go:
                    members = self.get_members(go)
                    group_manager = self.group_manager_info(go)
            else:
                errors.append(_('Desktop is not enabled for this group.'))

            brain = groupdict.get('brain')
            if brain:
                lapa = brain.landing_path
                if lapa:
                  refered = {
                    'title': brain.Title,
                    'path': lapa # or brain.getPath() + '/',
                    }

        pm = getToolByName(context, 'portal_membership')
        checkperm = pm.checkPermission
        perm = {
            'admin': group_manager and group_manager['id'] == user_id,
            'author': checkperm(ACCESS_DESKTOP, context),
            }
        res = {
            'groups': optgroups,
            'errors': errors,
            'current_group': groupdict,
            'group_manager': group_manager,
            'members': members,
            'userid': user_id,
            'perm': perm,
            'refered': refered,
            }
        return res

    def group_manager_info(self, go):
        """
        Currently we expect the group_manager to be a user
        """
        userid = go.getProperty('group_manager')
        if not userid:
            return None

        context = self.context
        puc = getToolByName(context, 'portal_user_catalog')
        brains = puc({
            'getUserId':   userid,
            'portal_type': 'UnitraccAuthor',
            })
        if not brains:
            logger.error('Profile of group manager %(userid)r not found!',
                         locals())
            return None
        brain = brains[0]
        return {
            'name':  get_title_and_name(brain),
            'id':    brain.getUserId,
            'email': brain.getEmail,
            'path':  brain.getPath(),
            'brain': brain,
            }

    def get_members(self, go):
        """
        Return a list of members of the given group
        """

        if not go:
            return []

        context = self.context
        puc = getToolByName(context, 'portal_user_catalog')
        members = []
        member_ids = go.getGroupMemberIds()
        for brain in puc({
            'getUserId': member_ids,
            getExcludeFromNav:   False,  # WIP: change index name
            'portal_type': 'UnitraccAuthor',
            }):
            members.append({
                'name':  get_title_and_name(brain),
                'id':    brain.getUserId,
                'email': brain.getEmail,
                'path':  brain.getPath(),
                'brain': brain,
                '_sort': joinNonemptyAttributes(brain,
                                                'getLastname', 'getFirstname',
                                                separator=', '),
                # 'uid': brain.UID,
                })
        members.sort(key=lambda x: (x['_sort'], x['id']))
        return members
