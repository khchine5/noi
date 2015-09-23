# -*- coding: UTF-8 -*-
# Copyright 2015 Luc Saffre
#
# This file is part of Lino Noi.
#
# Lino Noi is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Noi is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Noi.  If not, see
# <http://www.gnu.org/licenses/>.


from __future__ import unicode_literals

from lino.api import rt, dd, _
from lino.utils import Cycler


def objects():
    User = rt.modules.users.User
    # Company = rt.modules.contacts.Company
    Product = rt.modules.products.Product
    TT = rt.modules.tickets.TicketType
    Ticket = rt.modules.tickets.Ticket
    Interest = rt.modules.tickets.Interest
    Milestone = rt.modules.tickets.Milestone
    Project = rt.modules.tickets.Project
    Site = rt.modules.tickets.Site
    Link = rt.modules.tickets.Link
    LinkTypes = rt.modules.tickets.LinkTypes

    cons = rt.modules.users.UserProfiles.consultant
    dev = rt.modules.users.UserProfiles.developer
    yield User(username="mathieu", profile=cons)
    yield User(username="marc", profile=cons)
    yield User(username="luc", profile=dev)
    yield User(username="jean", profile=rt.modules.users.UserProfiles.senior)

    USERS = Cycler(User.objects.all())

    yield TT(**dd.str2kw('name', _("Bugfix")))
    yield TT(**dd.str2kw('name', _("Enhancement")))
    yield TT(**dd.str2kw('name', _("Upgrade")))

    TYPES = Cycler(TT.objects.all())

    yield Product(name="Lino Core", ref="linõ")
    yield Product(name="Lino Welfare", ref="welfäre")
    yield Product(name="Lino Cosi", ref="così")
    yield Product(name="Lino Faggio", ref="faggiö")

    PRODUCTS = Cycler(Product.objects.all())

    # kettenis = Company(name="ÖSHZ Kettenis")
    # yield kettenis
    # schaerbeek = Company(name="CPAS de Schaerbeek")
    # yield schaerbeek

    # yield Site(name="welket", partner=kettenis)
    # yield Site(name="welsch", partner=schaerbeek)

    yield Site(name="welket")
    yield Site(name="welsch")
    yield Site(name="pypi")

    for u in Site.objects.exclude(name="pypi"):
        for i in range(3):
            yield Interest(site=u, product=PRODUCTS.pop())

    SITES = Cycler(Site.objects.exclude(name="pypi"))
    for i in range(7):
        d = dd.today(i*2-20)
        yield Milestone(site=SITES.pop(), expected=d, reached=d)
    yield Milestone(site=SITES.pop(), expected=dd.today())

    yield Project(name="Framewörk", ref="linö", private=False)
    yield Project(name="Téam", ref="téam")
    yield Project(name="Documentatión", ref="docs", private=False)
    yield Project(name="Research", ref="research", private=False)
    yield Project(name="Shop", ref="shop", private=False)

    PROJECTS = Cycler(Project.objects.all())
    SITES = Cycler(Site.objects.all())

    def ticket(summary, **kwargs):
        site = SITES.pop()
        kwargs.update(
            ticket_type=TYPES.pop(), summary=summary,
            reporter=USERS.pop(),
            site=site,
            product=PRODUCTS.pop())
            
        if False:
            kwargs.update(project=PROJECTS.pop())
        return Ticket(**kwargs)

    welket = Site.objects.get(name="welket")
    yield ticket(
        "Föö fails to bar when baz", site=welket, project=PROJECTS.pop())
    yield ticket("Bar is not always baz", project=PROJECTS.pop())
    yield ticket("Baz sucks")
    yield ticket("Foo and bar don't baz", project=PROJECTS.pop())
    # a ticket without project:
    yield ticket("Cannot create Foo", description="""<p>When I try to create
    a <b>Foo</b>, then I get a <b>Bar</b> instead of a Foo.</p>""")

    yield ticket("Sell bar in baz", project=PROJECTS.pop())
    yield ticket("No Foo after deleting Bar", project=PROJECTS.pop())
    yield ticket("Is there any Bar in Foo?", project=PROJECTS.pop())
    yield ticket("Foo never matches Bar", project=PROJECTS.pop())
    yield ticket("Where can I find a Foo when bazing Bazes?",
                 project=PROJECTS.pop())
    yield ticket("Class-based Foos and Bars?", project=PROJECTS.pop())
    yield ticket("Foo cannot bar", project=PROJECTS.pop())

    # Example of memo markup:
    yield ticket("Bar cannot foo", project=PROJECTS.pop(),
                 description="""<p>Linking to [ticket 1] and to
                 [url http://luc.lino-framework.org/blog/2015/0923.html blog].</p>
                 """)
 
    yield ticket("Bar cannot baz", project=PROJECTS.pop())
    yield ticket("Bars have no foo", project=PROJECTS.pop())
    yield ticket("How to get bar from foo", project=PROJECTS.pop())

    yield Link(
        type=LinkTypes.requires,
        parent=Ticket.objects.get(pk=1),
        child=Ticket.objects.get(pk=2))