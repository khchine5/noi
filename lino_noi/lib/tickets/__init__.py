# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""Fixtures specific for the Team variant of Lino Noi.

.. autosummary::
   :toctree:

   models


"""

from lino_xl.lib.tickets import *

class Plugin(Plugin):

    extends_models = ['Ticket']
    
    needs_plugins = [
        'lino_xl.lib.excerpts',
        'lino_xl.lib.topics',
        'lino.modlib.comments', 'lino.modlib.changes',
        # 'lino_xl.lib.votes',
        'lino_noi.lib.noi']

    def setup_main_menu(self, site, user_type, m):
        super(Plugin, self).setup_main_menu(site, user_type, m)
        p = self.get_menu_group()
        m = m.add_menu(p.app_label, p.verbose_name)
        m.add_action('tickets.MyTicketsToWork')


    def get_dashboard_items(self, user):
        for i in super(Plugin, self).get_dashboard_items(user):
            yield i
        if user.authenticated:
            yield self.site.models.tickets.MyTicketsToWork
            # else:
            #     yield self.site.models.tickets.   PublicTickets

