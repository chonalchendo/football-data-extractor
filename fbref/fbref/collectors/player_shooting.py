from ..cleaners.common import common_cleaners
from ..cleaners.shooting import shooting_rename_cols
from ..schemas import ShootingStats
from .base import BasePlayerCollector


def shooting_collector() -> BasePlayerCollector:
    return BasePlayerCollector(
        stat="shooting",
        table="shooting",
        validator=ShootingStats,
        cleaners=common_cleaners + [shooting_rename_cols],
    )
