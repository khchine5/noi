# -*- coding: UTF-8 -*-
# Copyright 2014-2016 Luc Saffre
# License: BSD (see file COPYING for details)
"""
Database models for `lino_xl.lib.humanlinks`.

.. autosummary::

"""


from __future__ import unicode_literals
from __future__ import print_function

from django.utils.translation import string_concat
from django.db import models

from lino.modlib.system.choicelists import (
    ObservedEvent, PeriodStarted, PeriodActive, PeriodEnded)

from lino.api import dd, _
from .roles import Triager


from datetime import datetime, time
combine = datetime.combine
T00 = time(0, 0, 0)
T24 = time(23, 59, 59)


class TicketEvents(dd.ChoiceList):
    verbose_name = _("Observed event")
    verbose_name_plural = _("Observed events")


class TicketEventCreated(ObservedEvent):
    text = _("Created")

    def add_filter(self, qs, pv):
        if pv.start_date:
            qs = qs.filter(created__gte=combine(pv.start_date, T00))
        if pv.end_date:
            qs = qs.filter(created__lte=combine(pv.end_date, T24))
        return qs

TicketEvents.add_item_instance(TicketEventCreated('created'))


class TicketEventModified(ObservedEvent):
    text = _("Modified")

    def add_filter(self, qs, pv):
        if pv.start_date:
            qs = qs.filter(modified__gte=combine(pv.start_date, T00))
        if pv.end_date:
            qs = qs.filter(modified__lte=combine(pv.end_date, T24))
        return qs


TicketEvents.add_item_instance(TicketEventModified('modified'))


class ProjectEvents(dd.ChoiceList):
    verbose_name = _("Observed event")
    verbose_name_plural = _("Observed events")
    
ProjectEvents.add_item_instance(PeriodStarted('started'))
ProjectEvents.add_item_instance(PeriodActive('active'))
ProjectEvents.add_item_instance(PeriodEnded('ended'))
ProjectEvents.add_item_instance(TicketEventModified('modified'))


class TicketState(dd.State):
    active = False

   
class TicketStates(dd.Workflow):

    """The state of a ticket (new, open, closed, ...)

    Default choices are:

    .. attribute:: new

        Somebody reported this ticket, but there was no response so
        far.
        The ticket needs to be triaged.

    .. attribute:: talk

        The ticket needs discussion with the reporter.
        We don't yet know exactly
        what to do with it.

    .. attribute:: todo

        The ticket is confirmed and we are working on it.
        It appears in the todo list of somebody (either the assigned
        worker, or our general todo list)

    .. attribute:: testing

        The ticket is theoretically done, but we want to confirm this
        somehow, and it is not clear who (reporter, assignee or even
        some third user) should do the next step. If it is clear that
        the reporter should do the testing, then you should rather set
        the ticket to :attr:`talk`. If it is clear that you (the
        assignee) must test it, then leave the ticket at :attr:`todo`.

    .. attribute:: sleeping

        Waiting for some external event. We didn't decide what to do
        with it.

    .. attribute:: sticky

        Special state for permanent tickets which have no lifecycle.

    .. attribute:: ready

        The ticket is basically :attr:`done`, but some detail still
        needs to be done by the :attr:`reporter` (e.g. testing,
        confirmation, documentation,..)

    .. attribute:: done

        The ticket has been done.

    .. attribute:: cancelled

        It has been decided that we won't fix this ticket.

    """
    item_class = TicketState
    column_names = "value name text button_text active"
    active = models.BooleanField(_("Active"), default=False)
    required_roles = dd.required(dd.SiteStaff)
    

add = TicketStates.add_item

# add('10', _("Assigned"), 'assigned',
#     required=dict(states=['', 'active']),
#     action_name=_("Start"),
#     help_text=_("Ticket has been assigned to somebody who is assigned on it."))
add('10', _("New"), 'new',
    button_text=u"📥", active=True)  # INBOX TRAY (U+1F4E5)
add('15', _("Talk"), 'talk', active=True,
    button_text=u"🗪")  # TWO SPEECH BUBBLES (U+1F5EA)
add('20', _("ToDo"), 'todo', active=True,
    button_text=u"🐜")  # ANT (U+1F41C)
add('21', _("Sticky"), 'sticky',
    button_text=u"📌", active=True)  # PUSHPIN (U+1F4CC)
add('30', _("Sleeping"), 'sleeping',
    # button_text=u"🐌")  # SNAIL (U+1F40C)
    button_text=u"🕸")  # SPIDER WEB (U+1F578)	
# add('30', _("Callback"), 'callback',
    # required=dict(states=['new']),
    # action_name=_("Wait for feedback"),
    # help_text=_("Waiting for feedback from partner."))
add('40', _("Ready"), 'ready',
    # help_text=_(
    #     "Has been fixed. Ready for release. Waiting to be tested."),
    active=True,
    button_text="\u2610")  # BALLOT BOX
add('50', _("Done"), 'done',
    button_text="\u2611")  # BALLOT BOX WITH CHECK

# add('50', _("Tested"), 'tested',
#     # required=dict(states=['fixed']),
#     help_text=_("Has been fixed and tested."))
# add('60', _("Refused"), 'refused',
add('60', _("Cancelled"), 'cancelled',
    # required=dict(states="tested new todo callback"),
    # help_text=_("It has been decided that we won't fix this ticket."))
    button_text=u"🗑")  # WASTEBASKET (U+1F5D1)
# add('90', _("Cancelled"), 'cancelled',
#     # required=dict(states=['new todo waiting']),
#     help_text=_("Has been cancelled for some reason."))

"""Difference between Cancelled and Refused was that: Canceled means
that we don't want to talk about this ticket anymore.  Refused makes
sense for tickets which had been asked by a partner. In that case we
still may want to report it.

Also remember this thought: Should we add a new ticket state "dropped"
or "withdrawn" ("Verworfen", "Widerrufen") to indicate that the
*reporter* decided to cancel their plea? This is different from
"refused".  --> Solution seems to rename "refused" to "cancelled"
because this is a more general term.

"""


class MarkDone(dd.ChangeStateAction):
    """Mark this ticket as done. Can be done only by the reporter when a
    rating has been set or by a triager (independently of any rating).

    """
    label = _("Done")
    button_text = TicketStates.done.button_text
    required_states = 'ready'

    def get_action_permission(self, ar, obj, state):
        me = ar.get_user()
        if not me.profile.has_required_roles([Triager]):
            if not obj.rating or obj.reporter != me:
                return False
        return super(MarkDone, self).get_action_permission(ar, obj, state)


# class TicketStateGroups(dd.Choice):
#     def __init__(self, 
# class TicketStateGroups(dd.ChoiceList):
#     verbose_name = _("Dependency type")
# add = DependencyTypes.add_item
# add('10', _("Duplicate"), 'duplicate')


@dd.receiver(dd.pre_analyze)
def tickets_workflows(sender=None, **kw):
    """
    """
    TicketStates.sticky.add_transition(
        required_states="new")
    TicketStates.talk.add_transition(
        required_states="new todo ready")
    TicketStates.todo.add_transition(
        required_states="new talk ready")
    # TicketStates.cancelled.add_transition(states="todo new callback")
    # TicketStates.new.add_transition(states="todo callback fixed tested")
    TicketStates.sleeping.add_transition(
        required_states="talk todo new talk")
    TicketStates.ready.add_transition(
        required_states="new talk todo")
    TicketStates.done.add_transition(MarkDone)
    # TicketStates.done.add_transition(
    #     required_states="new talk todo ready sleeping")
    TicketStates.cancelled.add_transition(
        required_states="todo talk new talk sleeping")

    TicketStates.favorite_states = (TicketStates.sticky, )
    TicketStates.work_states = (TicketStates.todo, TicketStates.new)
    TicketStates.waiting_states = (TicketStates.done, )

    # not used:
    # TicketStates.idle_states = (
    #     TicketStates.fixed, TicketStates.tested,
    #     TicketStates.callback, TicketStates.cancelled)


class LinkType(dd.Choice):

    symmetric = False

    def __init__(self, value, name, ptext, ctext, **kw):
        self.ptext = ptext  # parent
        self.ctext = ctext
        # text = string_concat(ptext, ' (', ctext, ')')
        text = ptext
        super(LinkType, self).__init__(value, text, name, **kw)

    def as_parent(self):
        return self.ptext

    def as_child(self):
        return self.ctext


class LinkTypes(dd.ChoiceList):
    """The possible values of a :class:`lino_noi.lib.tickets.models.Link`.

    .. attribute:: requires

        The parent ticket requires the child ticket.
    
    .. attribute:: triggers

        The parent ticket triggers the child ticket.
    
    .. attribute:: deploys

        The parent ticket is a deployment which deploys the child ticket.

        Release notes are a printout of a deployment ticket which
        lists the deployed tickets.

    """
    required_roles = dd.required(dd.SiteStaff)
    verbose_name = _("Dependency type")
    verbose_name_plural = _("Dependency types")
    item_class = LinkType

add = LinkTypes.add_item
add('10', 'requires', _("Requires"), _("Required by"))
add('20', 'triggers', _("Triggers"), _("Triggered by"))
add('30', 'suggests', _("Suggests"), _("Suggested by"))
add('40', 'obsoletes', _("Obsoletes"), _("Obsoleted by"))
# add('30', 'seealso', _("See also"), _("Referred by"))
# deprecated (use "fixed_for" field instead):
# add('40', 'deploys', _("Deploys"), _("Deployed by"))
# replaced by FK field "duplicate_of"):
# add('50', 'duplicates', _("Duplicates"), _("Duplicate of"))

# LinkTypes.addable_types = [LinkTypes.requires, LinkTypes.duplicates]


class Ratings(dd.ChoiceList):
    verbose_name = _("Rating")
    verbose_name_plural = _("Ratings")

    
add = Ratings.add_item
add('10', _("Very good"))
add('20', _("Good"))
add('30', _("Satisfying"))
add('40', _("Deficient"))
add('50', _("Insufficient"))
add('90', _("Unratable"))


