from collections.abc import Sequence
from functools import partial
from typing import Callable

from bs4 import BeautifulSoup
from polars import DataFrame

from ._ages import parse_ages
from ._countries import parse_countries
from ._current_clubs import parse_current_club
from ._foots import parse_foot
from ._heights import parse_heights
from ._joined_dates import parse_joined_date
from ._names import parse_names
from ._numbers import parse_numbers
from ._positions import parse_positions
from ._signing_info import parse_signing_info
from ._tm_ids import parse_transfermarkt_id
from ._tm_names import parse_transfermarkt_name
from ._values import parse_market_values
from ._squad_names import get_squad_name

PARSER = Callable[[BeautifulSoup], DataFrame]


def get_squad_parsers(index: str) -> Sequence[PARSER]:
    return (
        partial(parse_ages, index=index),
        partial(parse_countries, index=index),
        partial(parse_current_club, index=index),
        partial(parse_foot, index=index),
        partial(parse_heights, index=index),
        partial(parse_joined_date, index=index),
        parse_names,
        partial(parse_numbers, index=index),
        parse_positions,
        partial(parse_signing_info, index=index),
        parse_transfermarkt_id,
        parse_transfermarkt_name,
        parse_market_values,
    )


__all__ = ["get_squad_parsers", "get_squad_name"]
