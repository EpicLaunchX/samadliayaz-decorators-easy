from pytemplate.domain.models import Movie, movie_factory  # noqa
from pytemplate.entrypoints.cli.main import main  # noqa
from pytemplate.service.tickets import buy_ticket_for_children, buy_ticket_for_teens  # noqa
from pytemplate.utils.decorator import age_limit_6plus, age_limit_13plus  # noqa

__version__ = "0.0.1"
