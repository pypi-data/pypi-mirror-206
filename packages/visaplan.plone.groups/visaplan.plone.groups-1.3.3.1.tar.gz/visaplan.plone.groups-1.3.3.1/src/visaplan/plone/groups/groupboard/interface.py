# -*- coding: utf-8 -*- Umlaute: ÄÖÜäöüß

# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.interface import Interface


class IGroupBoard(Interface):
    """

    """

    def viewBoard(self):
        """
        generelle Ansicht des Forums
        """

    def newThread(self):
        """
        neues Thema eröffnen
        """

    def replyThread(self, tid=None):
        """
        Antwort auf ein Thema schreiben
        """

    def save(self):
        """
        Neues Thema speichern
        """

    def save_reply(self):
        """
        Speichern einer Antwort
        """

    def get_messages(self, group_id=None, subject_id=None, all=None):
        """
        Hole alle Nachrichten aus der Datenbank.
        Falls Gruppe angegeben nur für Gruppe.
        Falls subject_id angegeben hole Thema für
        antwort ausgabe.
        """

    def get_group_id(self, subject_id):
        """
        Ermittle die Gruppen-ID für den angegebenen Thread
        """

    def editThread(self):
        """
        Einen Thread inklusive Titel bearbeiten
        """

    def delete_thread(self):
        """
        Einen Thread löschen.
        """

    def delete_post(self, mid=None, tid=None, withoutreturn=None):
        """
        Delete a single message
        """
