# -*- coding: UTF-8 -*-
# generated by lino.sphinxcontrib.help_text_builder
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
help_texts = {
    'lino_noi.lib.clocking.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_noi.lib.clocking.Plugin.ticket_model' : _("""The model that is to be used as the "workable"."""),
    'lino_noi.lib.clocking.actions.EndSession' : _("""Close a given session, i.e. stop working on that ticket for this
time.  Common base for EndThisSession and
EndTicketSession."""),
    'lino_noi.lib.clocking.actions.EndThisSession' : _("""Close this session, i.e. stop working on that ticket for this time."""),
    'lino_noi.lib.clocking.actions.EndTicketSession' : _("""End your running session on this ticket."""),
    'lino_noi.lib.clocking.actions.StartTicketSession' : _("""Start a session on this ticket."""),
    'lino_noi.lib.clocking.actions.PrintActivityReport' : _("""Print an activity report."""),
    'lino_noi.lib.clocking.mixins.Workable' : _("""Base class for things that workers can work on."""),
    'lino_noi.lib.clocking.models.SessionType' : _("""The type of a Session."""),
    'lino_noi.lib.clocking.models.Session' : _("""A Session is when a user works during a given lapse of time on
a given Ticket."""),
    'lino_noi.lib.clocking.models.Session.break_time' : _("""The time (in hh:mm) to remove from the duration resulting
from the difference between start_time and
end_time."""),
    'lino_noi.lib.clocking.models.Session.faculty' : _("""The faculty that has been used during this session. On a new
session this defaults to the needed faculty currently specified
on the ticket."""),
    'lino_noi.lib.clocking.roles.Worker' : _("""A user who is candidate for working on a ticket."""),
    'lino_noi.lib.clocking.ui.TicketHasSessions' : _("""Select only tickets for which there has been at least one session
during the given period."""),
    'lino_noi.lib.clocking.ui.ProjectHasSessions' : _("""Select only projects for which there has been at least one session
during the given period."""),
    'lino_noi.lib.clocking.ui.SessionsByTicket' : _("""The "Sessions" panel in the detail of a ticket."""),
    'lino_noi.lib.clocking.ui.SessionsByTicket.slave_summary' : _("""This panel shows:"""),
    'lino_noi.lib.clocking.ui.SessionsByTicket.master' : _("""alias of Ticket"""),
    'lino_noi.lib.clocking.ui.SessionsByTicket.model' : _("""alias of Session"""),
    'lino_noi.lib.deploy.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_noi.lib.deploy.desktop.Milestones.model' : _("""alias of Milestone"""),
    'lino_noi.lib.deploy.models.Milestone' : _("""A Milestone is a named step of evolution on a given Site.  For
software projects we usually call them a "release" and they are
named by a version number."""),
    'lino_noi.lib.deploy.models.Milestone.closed' : _("""Closed milestones are hidden in most lists."""),
    'lino_noi.lib.deploy.models.Deployment' : _("""A deployment is the fact that a given ticket is being fixed (or
installed or activated) by a given milestone (to a given site)."""),
    'lino_noi.lib.deploy.models.Deployment.milestone' : _("""The milestone (and site) of this deployment."""),
    'lino_noi.lib.faculties.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_noi.lib.faculties.models.Faculty' : _("""A faculty is a knowledge or ability which can be required in
order to work e.g. on some ticket, and which individual users can
have or not."""),
    'lino_noi.lib.faculties.models.Competence' : _("""A competence is when a given user is declared to be competent
in a given faculty."""),
    'lino_noi.lib.noi.migrate.Migrator' : _("""The standard migrator for noi."""),
    'lino_noi.lib.noi.user_types.EndUser' : _("""An end user is somebody who uses our software and may report
tickets, but won't work on them."""),
    'lino_noi.lib.noi.user_types.Consultant' : _("""A consultant is somebody who may both report tickets and work
on them."""),
    'lino_noi.lib.noi.user_types.Developer' : _("""A developer is somebody who may both report tickets and work
on them."""),
    'lino_noi.lib.noi.user_types.Senior' : _("""A senior developer is a developer who is additionally
responsible for triaging tickets"""),
    'lino_noi.lib.noi.user_types.SiteAdmin' : _("""Can do everything."""),
    'lino_noi.lib.noi.workflows.TicketAction' : _("""Base class for ticket actions."""),
    'lino_noi.lib.noi.workflows.MarkTicketOpened' : _("""Mark this ticket as open."""),
    'lino_noi.lib.noi.workflows.MarkTicketStarted' : _("""Mark this ticket as started."""),
    'lino_noi.lib.noi.workflows.MarkTicketReady' : _("""Mark this ticket as ready."""),
    'lino_noi.lib.noi.workflows.MarkTicketClosed' : _("""Mark this ticket as closed."""),
    'lino_noi.lib.noi.workflows.MarkTicketTalk' : _("""Mark this ticket as talk."""),
    'lino_noi.lib.noi.workflows.MarkVoteRated' : _("""Rate this vote and mark it as rated."""),
    'lino_noi.lib.noi.workflows.MarkVoteRated.rating' : _("""How you rate this job."""),
    'lino_noi.lib.noi.workflows.MarkVoteRated.comment' : _("""Your comment related to your rating."""),
    'lino_noi.lib.tickets.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_noi.lib.tickets.choicelists.TicketStates' : _("""The state of a ticket (new, open, closed, ...)"""),
    'lino_noi.lib.tickets.choicelists.TicketStates.new' : _("""Somebody reported this ticket, but there was no response so
far.
The ticket needs to be triaged."""),
    'lino_noi.lib.tickets.choicelists.TicketStates.talk' : _("""Some worker needs discussion with the author.  We don't yet
know exactly what to do with it."""),
    'lino_noi.lib.tickets.choicelists.TicketStates.todo' : _("""The ticket is confirmed and we are working on it.
It appears in the todo list of somebody (either the assigned
worker, or our general todo list)"""),
    'lino_noi.lib.tickets.choicelists.TicketStates.testing' : _("""The ticket is theoretically done, but we want to confirm this
somehow, and it is not clear who should do the next step. If
it is clear that the author should do the testing, then you
should rather set the ticket to talk. If it is clear
that you (the assignee) must test it, then leave the ticket at
todo."""),
    'lino_noi.lib.tickets.choicelists.TicketStates.sleeping' : _("""Waiting for some external event. We didn't decide what to do
with it."""),
    'lino_noi.lib.tickets.choicelists.TicketStates.sticky' : _("""Special state for permanent tickets which have no lifecycle."""),
    'lino_noi.lib.tickets.choicelists.TicketStates.ready' : _("""The ticket is basically done, but some detail still
needs to be done by the user (e.g. testing,
confirmation, documentation,..)"""),
    'lino_noi.lib.tickets.choicelists.TicketStates.done' : _("""The ticket has been done."""),
    'lino_noi.lib.tickets.choicelists.TicketStates.cancelled' : _("""It has been decided that we won't fix this ticket."""),
    'lino_noi.lib.tickets.choicelists.LinkTypes' : _("""The possible values of a lino_noi.lib.tickets.models.Link."""),
    'lino_noi.lib.tickets.choicelists.LinkTypes.requires' : _("""The parent ticket requires the child ticket."""),
    'lino_noi.lib.tickets.choicelists.LinkTypes.triggers' : _("""The parent ticket triggers the child ticket."""),
    'lino_noi.lib.tickets.choicelists.LinkTypes.deploys' : _("""The parent ticket is a deployment which deploys the child ticket."""),
    'lino_noi.lib.tickets.models.TimeInvestment' : _("""Model mixin for things which represent a time investment.  This
currently just defines a group of three fields:"""),
    'lino_noi.lib.tickets.models.TimeInvestment.closed' : _("""Whether this investment is closed, i.e. certain things should
not change anymore."""),
    'lino_noi.lib.tickets.models.TimeInvestment.private' : _("""Whether this investment is private, i.e. should not be
publicly visible anywhere."""),
    'lino_noi.lib.tickets.models.TimeInvestment.planned_time' : _("""The time (in hours) we plan to work on this project or ticket."""),
    'lino_noi.lib.tickets.models.ProjectType' : _("""The type of a Project."""),
    'lino_noi.lib.tickets.models.TicketType' : _("""The type of a Ticket."""),
    'lino_noi.lib.tickets.models.Project' : _("""A project is something on which several users work together."""),
    'lino_noi.lib.tickets.models.Project.assign_to' : _("""The user to whom new tickets will be assigned.
See Ticket.assigned_to."""),
    'lino_noi.lib.tickets.models.Ticket' : _("""A Ticket is a concrete question or problem formulated by a
user."""),
    'lino_noi.lib.tickets.models.Ticket.user' : _("""The user who entered this ticket and is responsible for
managing it."""),
    'lino_noi.lib.tickets.models.Ticket.end_user' : _("""The end user who is asking for help."""),
    'lino_noi.lib.tickets.models.Ticket.assigned_to' : _("""No longer used. The user who is working on this ticket."""),
    'lino_noi.lib.tickets.models.Ticket.state' : _("""The state of this ticket. See TicketStates"""),
    'lino_noi.lib.tickets.models.Ticket.waiting_for' : _("""What to do next. An unformatted one-line text which describes
what this ticket is waiting for."""),
    'lino_noi.lib.tickets.models.Ticket.upgrade_notes' : _("""A formatted text field meant for writing instructions for the
hoster's site administrator when doing an upgrade where this
ticket is being deployed."""),
    'lino_noi.lib.tickets.models.Ticket.description' : _("""A complete and concise description of the ticket. This should
describe in more detail what this ticket is about. If the
ticket has evolved during time, it should reflect the latest
version."""),
    'lino_noi.lib.tickets.models.Ticket.duplicate_of' : _("""A pointer to the ticket which is the cause of this ticket."""),
    'lino_noi.lib.tickets.models.Ticket.deadline' : _("""Specify that the ticket must be done for a given date."""),
    'lino_noi.lib.tickets.models.Ticket.priority' : _("""How urgent this ticket is. This should be a value between 0
and 100."""),
    'lino_noi.lib.tickets.models.Ticket.rating' : _("""How the author rates this ticket."""),
    'lino_noi.lib.tickets.roles.TicketsUser' : _("""A user who can create new tickets."""),
    'lino_noi.lib.tickets.roles.Searcher' : _("""A user who can see all tickets."""),
    'lino_noi.lib.tickets.roles.Triager' : _("""A user who is responsible for triaging new tickets."""),
    'lino_noi.lib.tickets.roles.TicketsStaff' : _("""Can configure tickets functionality."""),
    'lino_noi.lib.tickets.ui.ActiveProjects' : _("""Show a list of active projects."""),
    'lino_noi.lib.tickets.ui.ActiveProjects.model' : _("""alias of Project"""),
    'lino_noi.lib.tickets.ui.Tickets' : _("""Global list of all tickets."""),
    'lino_noi.lib.tickets.ui.Tickets.site' : _("""Select a site if you want to see only tickets for this site."""),
    'lino_noi.lib.tickets.ui.Tickets.show_private' : _("""Show only (or hide) tickets that are marked private."""),
    'lino_noi.lib.tickets.ui.Tickets.show_todo' : _("""Show only (or hide) tickets which are todo (i.e. state is New
or ToDo)."""),
    'lino_noi.lib.tickets.ui.Tickets.show_active' : _("""Show only (or hide) tickets which are active (i.e. state is Talk
or ToDo)."""),
    'lino_noi.lib.tickets.ui.Tickets.show_assigned' : _("""Show only (or hide) tickets which are assigned to somebody."""),
    'lino_noi.lib.tickets.ui.Tickets.has_project' : _("""Show only (or hide) tickets which have a project assigned."""),
    'lino_noi.lib.tickets.ui.Tickets.feasable_by' : _("""Show only tickets for which I am competent."""),
    'lino_noi.lib.tickets.ui.Tickets.model' : _("""alias of Ticket"""),
    'lino_noi.lib.tickets.ui.DuplicatesByTicket' : _("""Shows the tickets which are marked as duplicates of this
(i.e. whose duplicate_of field points to this ticket."""),
    'lino_noi.lib.tickets.ui.DuplicatesByTicket.master' : _("""alias of Ticket"""),
    'lino_noi.lib.tickets.ui.DuplicatesByTicket.model' : _("""alias of Ticket"""),
    'lino_noi.lib.tickets.ui.SuggestedTickets' : _("""Shows the tickets of other users which need help on a faculty for
which I am competent."""),
    'lino_noi.lib.tickets.ui.SuggestedTickets.model' : _("""alias of Ticket"""),
    'lino_noi.lib.tickets.ui.TicketsToTriage' : _("""List of tickets that need to be triaged.  Currently this is
equivalent to those having their state set to new."""),
    'lino_noi.lib.tickets.ui.TicketsToTriage.model' : _("""alias of Ticket"""),
    'lino_noi.lib.tickets.ui.ActiveTickets' : _("""Show all tickets that are in an active state."""),
    'lino_noi.lib.tickets.ui.ActiveTickets.model' : _("""alias of Ticket"""),
    'lino_noi.lib.tickets.ui.MyTickets' : _("""Show all active tickets reported by me."""),
    'lino_noi.lib.tickets.ui.MyTickets.model' : _("""alias of Ticket"""),
    'lino_noi.lib.users.choicelists.UserStates' : _("""The list of possible choices for the state field
of a User."""),
    'lino_noi.lib.users.choicelists.MarkUserActive' : _("""Activate this user. This requires that the user has confirmed their
verifcation code, and that a username and password are set."""),
    'lino_noi.lib.users.desktop.UserDetail' : _("""Layout of User Detail in Lino Noi."""),
    'lino_noi.lib.users.desktop.RegisterUser' : _("""Fill a form in order to register as a new system user."""),
    'lino_noi.lib.users.desktop.NewUsers' : _("""List of new users to be confirmed by the system admin."""),
    'lino_noi.lib.users.desktop.NewUsers.model' : _("""alias of User"""),
    'lino_noi.lib.users.models.CheckedSubmitInsert' : _("""Like the standard lino.core.actions.SubmitInsert, but
checks certain things before accepting the new user."""),
    'lino_noi.lib.users.models.VerifyUser' : _("""Enter your verification code."""),
    'lino_noi.lib.users.models.User.callme_mode' : _("""Whether other users can see my contact data."""),
    'lino_noi.lib.users.models.User.verification_code' : _("""A random string set for every new user. Used for
online_registration."""),
    'lino_noi.lib.users.models.User.user_state' : _("""The registration state of this user."""),
    'lino_noi.lib.votes.Plugin' : _("""See lino.core.plugin.Plugin."""),
    'lino_noi.lib.votes.Plugin.votable_model' : _("""The things we are voting about. A string referring to the model
which represents a votable in your application.  Default value is
'tickets.Ticket' (referring to
lino_noi.lib.tickets.models.Ticket)."""),
    'lino_noi.lib.votes.actions.CreateVote' : _("""Define your vote about this object."""),
    'lino_noi.lib.votes.actions.VotableEditVote' : _("""Edit your vote about this object."""),
    'lino_noi.lib.votes.choicelists.VoteState' : _("""The state of a vote."""),
    'lino_noi.lib.votes.choicelists.VoteState.vote_name' : _("""Translatable text. How a vote is called when in this state."""),
    'lino_noi.lib.votes.choicelists.VoteStates' : _("""The list of possible states of a vote.  This is used as choicelist
for the state
field of a vote."""),
    'lino_noi.lib.votes.choicelists.VoteStates.author' : _("""Reserved for the author's vote.  Lino automatically creates an
author vote for every author of a ticket (see
get_vote_raters)."""),
    'lino_noi.lib.votes.choicelists.VoteStates.item_class' : _("""alias of VoteState"""),
    'lino_noi.lib.votes.mixins.Votable' : _("""Base class for models that can be used as
lino_noi.lib.votes.Plugin.votable_model."""),
    'lino_noi.lib.votes.models.Vote' : _("""A vote is when a user has an opinion or interest about a given
ticket (or any other votable)."""),
    'lino_noi.lib.votes.models.Vote.votable' : _("""The ticket (or other votable) being voted."""),
    'lino_noi.lib.votes.models.Vote.user' : _("""The user who is voting."""),
    'lino_noi.lib.votes.models.Vote.state' : _("""The state of this vote.  Pointer to VoteStates."""),
    'lino_noi.lib.votes.models.Vote.priority' : _("""My personal priority for this ticket."""),
    'lino_noi.lib.votes.models.Vote.rating' : _("""How the ticket author rates my help on this ticket."""),
    'lino_noi.lib.votes.models.Vote.remark' : _("""Why I am interested in this ticket."""),
    'lino_noi.lib.votes.models.Vote.nickname' : _("""My nickname for this ticket. Optional."""),
    'lino_noi.lib.votes.models.Votes' : _("""Table parameters:"""),
    'lino_noi.lib.votes.models.Votes.observed_event' : _("""There are two class attributes for defining a filter conditions
which canot be removed by the user:"""),
    'lino_noi.lib.votes.models.Votes.filter_vote_states' : _("""A set of vote states to require (i.e. to filter upon).  This
must resolve using resolve_states."""),
    'lino_noi.lib.votes.models.Votes.exclude_vote_states' : _("""A set of vote states to exclude.  This must
resolve using resolve_states."""),
    'lino_noi.lib.votes.models.Votes.filter_ticket_states' : _("""A set of ticket states to require (i.e. to filter upon). This
must resolve using resolve_states."""),
    'lino_noi.lib.votes.models.Votes.model' : _("""alias of Vote"""),
    'lino_noi.lib.votes.models.MyVotes' : _("""Show your votes in all states"""),
    'lino_noi.lib.votes.models.MyVotes.model' : _("""alias of Vote"""),
    'lino_noi.lib.votes.models.MyOffers' : _("""Show the tickets for which you are candidate"""),
    'lino_noi.lib.votes.models.MyOffers.model' : _("""alias of Vote"""),
    'lino_noi.lib.votes.models.MyTasks' : _("""Show your votes in states assigned and done"""),
    'lino_noi.lib.votes.models.MyTasks.model' : _("""alias of Vote"""),
    'lino_noi.lib.votes.models.MyWatched' : _("""Show your votes in states watching"""),
    'lino_noi.lib.votes.models.MyWatched.model' : _("""alias of Vote"""),
    'lino_noi.lib.votes.models.VotesByVotable' : _("""Show the votes about this object."""),
    'lino_noi.lib.votes.models.VotesByVotable.master' : _("""alias of Ticket"""),
    'lino_noi.lib.votes.models.VotesByVotable.model' : _("""alias of Vote"""),
    'lino_noi.projects.bs3.settings.demo.Site' : _("""Defines and instantiates a demo version of Lino Noi."""),
    'lino_noi.projects.care.settings.demo.Site' : _("""Defines and instantiates a demo version of Lino Care."""),
    'lino_noi.projects.care.user_types.SimpleUser' : _("""A simple user is a person who can log into the application in
order to manage their own pleas and competences and potentially
can respond to other user's pleas."""),
    'lino_noi.projects.care.user_types.Connector' : _("""A connector is a person who knows other persons and who
introduces pleas on their behalf."""),
    'lino_noi.projects.care.user_types.SiteAdmin' : _("""A site administrator can do everything."""),
    'lino_noi.projects.public.settings.demo.Site' : _("""Defines and instantiates a demo version of Lino Noi."""),
    'lino_noi.projects.team.lib.clocking.models.ServiceReport' : _("""A service report is a document used in various discussions with
a stakeholder."""),
    'lino_noi.projects.team.lib.clocking.models.ServiceReport.user' : _("""This can be empty and will then show the working time of all
users."""),
    'lino_noi.projects.team.lib.tickets.Plugin' : _("""Adds the lino_noi.lib.votes plugin."""),
    'lino_noi.projects.team.lib.tickets.models.TicketDetail' : _("""Customized detail_lyout for Tickets.  Replaces waiting_for by
faculties"""),
    'lino_noi.projects.team.settings.demo.Site' : _("""Defines and instantiates a demo version of Lino Noi."""),
}
