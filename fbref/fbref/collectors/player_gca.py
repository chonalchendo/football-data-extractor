from ..cleaners.common import common_cleaners
from ..cleaners.gca import gca_cleaners
from ..schemas import GcaStats
from .base import BasePlayerCollector

gca_collector = BasePlayerCollector(
    stat="gca", table="gca", validator=GcaStats, cleaners=common_cleaners + gca_cleaners
)
