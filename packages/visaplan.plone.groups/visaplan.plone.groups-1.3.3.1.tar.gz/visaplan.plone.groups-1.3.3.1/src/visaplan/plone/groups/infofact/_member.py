# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et hls tw=79
# visaplan.plone.groups:infofact: member information

# Python compatibility:
from __future__ import absolute_import

# visaplan:
from visaplan.plone.tools.groups import groupinfo_factory, userinfo_factory

__all__ = [
    'memberinfo_factory',
    ]

# ------------------------------- [ memberinfo_factory ... [
def memberinfo_factory(context, pretty=0, forlist=0, bloated=0):
    """
    Wie groupinfo_factory, aber für Gruppen- und Benutzerobjekte.
    Es wird zusätzlich ein Feld 'type' gefüllt, das die Werte
    'user', 'group' oder (mit bloated >= 2) None annehmen kann.

    Die folgenden beiden werden einfach an groupinfo_factory bzw.
    userinfo_factory weitergereicht:

    pretty -- Gruppennamen auflösen, wenn Suffix an ID und Titel;
              für benutzer: title als formatierter Name (author
    forlist -- Minimale Rückgabe (nur ID und Titel),
               aber mit pretty kombinierbar

    Zusätzliches Argument:

    bloated -- Schlüssel hinzufügen für Mitgliederliste wie in Tabelle
               unitracc_groupmemberships.
               Wenn >= 2, werden auch für nicht gefundene Mitglieder Einträge
               zurückgegeben (noch nicht getestet)

               ACHTUNG: Der Schlüssel 'ismember_zope' wird immer mit True
                        gefüllt (auch für nicht existierende); das stimmt, wenn
               die IDs aus einer Zope-Mitgliederliste der interessierenden
               Gruppe stammen. Wenn die IDs auch aus einer anderen Quelle
               kommen (z. B. einer Datenbankabfrage), muß dieser Wert
               anschließend noch manuell korrigiert werden!
    """
    ggibi = groupinfo_factory(context, pretty=pretty, forlist=forlist)
    guibi = userinfo_factory(context, pretty=pretty, forlist=forlist)

    # ggibi gibt (für Gruppen) keinen title-Schlüssel zurück:
    g_title_key = (pretty and 'pretty_title'
                           or 'group_title')

    def basic_member_info(member_id):
        """
        Basisinformationen über ein "Member" (Benutzer oder Gruppe):
        id, title, type

        Suche zuerst einen Benutzer, dann als Rückfalloption eine Gruppe
        """
        member = guibi(member_id)
        if member is not None:
            member['type'] = 'user'
            return member
        member = ggibi(member_id)
        if member:
            member['type'] = 'group'
            member['title'] = member[g_title_key]
            return member
        else:
            return None  # PEP 20.2

    def bloated_member_info(member_id):
        """
        Gib dict-Objekt zurück wie nach dem Einfügen in
        die Tabelle unitracc_groupmemberships erzeugt
        """
        member = basic_member_info(member_id)
        if member is not None:
            member.update({'member_id_': member_id,
                           'start': None,
                           'ends': None,
                           'active': True,
                           'ismember_zope': True,
                           })
            return member
        elif bloated >= 2:
            return {'id': member_id,
                    'member_id_': member_id,
                    'title': 'not found: %(member_id)s'
                             % locals(),
                    g_title_key: None,
                    'type': None,
                    'ismember_zope': True,
                    'active': None,
                    'start': None,
                    'ends': None,
                    }

    if bloated:
        return bloated_member_info
    else:
        return basic_member_info
# ------------------------------- ] ... memberinfo_factory ]
