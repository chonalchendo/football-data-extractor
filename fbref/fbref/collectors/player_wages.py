from ..cleaners.common import wage_cleaners
from ..cleaners.wages import wages_rename_cols
from ..schemas import WageStats
from .base import BasePlayerCollector, WageParams
from ..constants import PLAYER_WAGES_URL


def wage_collector(comp_id: str, comp_name: str) -> BasePlayerCollector:
    return BasePlayerCollector(
        url=PLAYER_WAGES_URL,
        url_params=WageParams(comp_id=comp_id, comp_name=comp_name),
        validator=WageStats,
        cleaners=wage_cleaners + [wages_rename_cols],
    )
