# Python compatibility:
from __future__ import absolute_import

# Zope:
from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.interface import implements

# Local imports:
from ..interfaces import IMyCalendar


class MyCalendar(BrowserView):
    implements(IMyCalendar)

    def data(self):
        """
        Provide data for ./mytalk.pt
        """
        context = self.context
        pm = getToolByName(context, 'portal_membership')
        if pm.isAnonymousUser():
            raise Unauthorized
