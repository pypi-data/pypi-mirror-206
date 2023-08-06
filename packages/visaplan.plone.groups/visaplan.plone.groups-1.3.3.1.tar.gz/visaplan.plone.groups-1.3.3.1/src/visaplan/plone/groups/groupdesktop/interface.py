# -*- coding: utf-8 -*- Umlaute: ÄÖÜäöüß
# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.interface import Interface


class IGroupDesktop(Interface):

    def getInfo(topic=None,
                tid=None,
                portal_type=None,
                get_members=0):
        """
        Gib ein Python-Dictionary zurueck, das interessante
        Informationen fuer den Gruppenschreibtisch enthaelt
        """

    def getLoopDicts(gid=None, topic=None, exclude=None):
        """
        Gib Dictionarys fuer group-desktop zurueck
        """

    def getGroupsBlacklist():
        """
        Gib die Gruppen zurueck, die *keine* Gruppenschreibtische erzeugen
        """

    def groupProvidesMembers(gid):
        """
        Stellt die uebergebene Gruppe ueber ihren Gruppenschreibtisch
        die Visitenkarten ihrer Mitglieder zur Verfuegung?
        """

    def can_view_group_administration(group_id, user_id=None):
        """
        Kann Benutzer Gruppenschreibtisch administrieren? ja/nein
        """

    def auth_view_group_administration(group_id, user_id=None):
        """
        Kann Benutzer Gruppenschreibtisch administrieren? ja/nein;
        wenn nein -> Unauthorized-Exception
        """

    def set_end_of_group_membership_to_today():
        """
        Mitgliedschaft durch Gruppenadministrator beeenden.
        """
