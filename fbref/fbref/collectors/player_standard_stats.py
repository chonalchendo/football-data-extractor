from ..cleaners.common import common_cleaners
from ..cleaners.standard import standard_rename_cols
from ..schemas import StandardStats
from .base import BasePlayerCollector

standard_stats_collector = BasePlayerCollector(
    stat="stats",
    table="standard",
    validator=StandardStats,
    cleaners=common_cleaners + [standard_rename_cols],
)
