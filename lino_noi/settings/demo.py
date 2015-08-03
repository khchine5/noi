import datetime

from lino_noi.settings import *


class Site(Site):
    """Defines and instantiates a demo version of Lino Noi."""

    the_demo_date = datetime.date(2015, 5, 23)

    languages = "en de fr"

    def setup_plugins(self):
        """Change the default value of certain plugin settings.

        - :attr:`excerpts.responsible_user
          <lino.modlib.excerpts.Plugin.responsible_user>` is set to
          ``'jean'`` who is both senior developer and site admin in
          the demo database.

        """
        super(Site, self).setup_plugins()
        self.plugins.excerpts.configure(responsible_user='jean')


SITE = Site(globals())

# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'
