from collections.abc import Sequence

from ..base import Parser
from ._ages import Ages
from ._countries import Countries
from ._current_clubs import CurrentClubs
from ._foots import Foot
from ._heights import Heights
from ._joined_dates import JoinedDate
from ._names import Names
from ._numbers import Numbers
from ._positions import Positions
from ._signing_info import SigningInfo
from ._tm_ids import TransfermarktId
from ._tm_names import TransfermarktName
from ._values import Values
from ._squad_names import get_squad_name

squad_parsers: Sequence[Parser] = (
    Ages(),
    Countries(),
    CurrentClubs(),
    Heights(),
    Names(),
    Positions(),
    Values(),
    JoinedDate(),
    Numbers(),
    SigningInfo(),
    TransfermarktId(),
    TransfermarktName(),
    Foot(),
)

__all__ = [
    "squad_parsers",
    "get_squad_name"
]
