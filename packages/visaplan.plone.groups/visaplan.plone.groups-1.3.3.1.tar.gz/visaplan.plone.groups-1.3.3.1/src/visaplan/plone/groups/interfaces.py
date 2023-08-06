# -*- coding: utf-8 -*- äöü
"""Module where all interfaces, events and exceptions live."""

# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.interface import Interface


class IMyCalendar(Interface):
    """
    View the "forums" for all desktop-enabled groups the logged-in user is
    member of.
    """


class IMyFellows(Interface):
    """
    View the fellow group members who have opted in to be visible
    """
