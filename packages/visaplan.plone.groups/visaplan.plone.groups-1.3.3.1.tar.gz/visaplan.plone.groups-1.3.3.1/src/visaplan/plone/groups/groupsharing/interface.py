# -*- coding: utf-8 -*- Umlaute: ÄÖÜäöüß

# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.interface import Interface


class IGroupSharing(Interface):

    def canManage(self):
        """
        Darf der angemeldete Benutzer diese Gruppe bzw., wenn keine angegeben:
        alle Gruppen bearbeiten?
        """

    def authManage(self):
        """
        Wirft ggf. Unauthorized
        """

    def get_group_info_by_id(self, group_id, pretty=0, getObject=0):
        """
        Gib ein Dict. zurück;
        - immer vorhandene Schlüssel: id, group_title, group_description
        - nur bei automatisch erzeugten Gruppen: role, role_translation, brain
        """

    def get_groups_by_user_id(self, user_id, explicit=True, askdb=None):
        """
        Gib eine sortierte Liste von Gruppen-Info-Dictionarys zurück.
        """

    def get_user_and_all_groups(self, uogid):
        """
        Ermittle die IDs aller Gruppen, denen der übergebene User (oder die
        Gruppe -- uogid) angehört - abzgl. der üblichen Ausnahme
        'AuthenticatedUsers'.
        Gib ein 2-Tupel zurück:

        (user_id, set(group_ids))

        Wenn die übergebene ID <uogid> zu einem User gehört, wird sie aus dem
        Set der Gruppen-IDs entfernt und im ersten Teil des Tupels
        zurückgegeben; ansonsten ist dieser erste Teil None.
        """

    def delete_group_membership_by_group_id(self):
        """
        Aufgerufen aus manage_group_view;
        die Gruppenzuordnungen sollen hier *tatsächlich*
        spurlos beseitigt werden! (Aufräumfunktion)

        Formularfelder:
        ids -- eine Liste von Member-IDs
        group_id -- die aufzuräumende Gruppe
        """

    def add_group_membership(self):
        """
        Füge *einen* Benutzer (oder eine Gruppe)
        einer oder mehreren Gruppen hinzu

        Startdatum ist heute;
        ein Endedatum wird nicht gesetzt.

        Siehe auch --> add_to_group (mehrere Benutzer, eine Gruppe,
        variable Datumswerte)
        """

    def end_group_memberships(self):
        """
        *Beende* Gruppenmitgliedschaften (ohne sie spurlos zu entfernen)
        """

    def delete_group_memberships(self):
        """
        Zum Aufruf aus Formularen: *Entferne* Gruppenmitgliedschaften
        (und lösche sie aus der relationalen Datenbank)
        """

    def search_groups(self, string_='', sort_=True):
        """ """

    def get_explicit_group_memberships(self, group_id):
        """
        gib die Benutzer und Gruppen zurück, die direkte Mitglieder
        der übergebenen Gruppe sind
        """

    def search_groups_and_users(self, string_=''):
        """ """

    def add_to_group(self):
        """
        Füge Benutzer und/oder Gruppen einer Gruppe hinzu.
        Formulardaten:

        Formular   | Feldname   | Erklärung
        -----------+------------+----------------------------------------
        group_id   | group_id_  | ursprünglich ging es nur um Kursgruppen
        ids:list   | member_id_ | ursprünglich "(Schul-) Klassen", jetzt
                   |            | allgemein Benutzer- oder Gruppen-IDs
        start_<id> | start      | Startdatum, d.m.yyyy, default: heute
        end_<id>   | ends       | Ablaufdatum, d.m.yyyy, default: leer
        """

    def delete_groups(self):
        """ """

    def update_group(self):
        """ """

    def can_view_unitracc_groups(self):
        """
        für Schema: regelt den Zugriff auf das Gruppenfreigabe-Widget
        """

    def get_permission_authors(self):
        """ """

    def get_custom_search_authors(self):
        """ """

    def get_group_memberships(self, group_id, explicit=True):
        """
        Gib alle Gruppen zurück, deren direktes Mitglied die
        übergebene Gruppe ist
        (ACHTUNG, Argument 'explicit' wird bisher nicht berücksichtigt!)
        """

    def connect_groups(self):
        """ Verbindet manuell erstellte Gruppen mit automatisch erstellten Kursgruppen. """

    def disconnect_groups(self):
        """
        Trennt manuell erstellte Gruppen von automatisch erstellten Kursgruppen.
        """

    def scheduled_group_memberships(self):
        """
        Arbeite die Gruppenzuordnungen ab gemäß der Tabelle
        unitracc_groupmemberships (neuer cron-Job).
        """

    def update_view_duration(self):
        """
        Übergib Formulardaten an --> _update_view_duration
        """

    def _update_view_duration(group_id, member_id,
                              sql,
                              start=None, ends=None, TODAY=None):
        """
        - Füge der Gruppe <group_id> das Mitglied <member_id> hinzu
          (wenn die weiteren übergebenen Datumswerte None sind)
          oder entferne es,
        - pflege die entsprechenden Werte in die Tabelle
          unitracc_groupmemberships ein,
          und
        - schreibe einen entsprechenden Absatz nach var/log/groups.txt
        """

    def replay_groups(self):
        """
        Gruppenzuordnungen "nachholen".  Da die Formulardaten Datumswerte
        enthalten können, darf das nur von einem Admin gemacht werden.
        """

    def get_course_info_for_group_ids(self, group_ids):
        """ """

    def get_group_manager_for_group_id(self, group_id):
        """ """

    def is_member_of_any(self, group_ids, user_id=None, default=False):
        """
        Ist der übergebene Benutzer Mitglied einer der übergebenen Gruppen?

        - wenn user_id nicht übergeben wird, wird der angemeldete Benutzer
          verwendet
        - wenn die Liste der Gruppen-IDs leer ist, wird der Vorgabewert
          verwendet (default)
        """

