from ..cleaners.common import common_cleaners
from ..cleaners.misc import misc_rename_cols
from ..schemas import MiscStats
from .base import BasePlayerCollector

misc_collector = BasePlayerCollector(
    stat="misc",
    table="misc",
    validator=MiscStats,
    cleaners=common_cleaners + [misc_rename_cols],
)
