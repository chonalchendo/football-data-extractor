from ..cleaners.common import common_plus_xg_cleaners
from ..cleaners.passing import passing_rename_cols
from ..schemas import PassingStats
from .base import BasePlayerCollector

passing_collector = BasePlayerCollector(
    stat="passing",
    table="passing",
    validator=PassingStats,
    cleaners=common_plus_xg_cleaners + passing_rename_cols,
)
