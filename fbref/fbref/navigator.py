import importlib
import time

from rich import print

from .collectors.base import BasePlayerCollector
from .feeds import Feed
from .utils.logger import get_logger

logger = get_logger(__name__)


class NavigatorRunner:
    """
    NavigatorRunner is a class that is responsible for running the fbref data collectors -
    analogous to a spider in a web scraping framework. It is responsible for navigating to the
    desired collector, starting the collection process, and writing the data to a file.
    """

    def __init__(self, feed: Feed, download_delay: int | None = None) -> None:
        self.feed = feed
        self.download_deplay = download_delay
        self._collector: str | None = None
        self._collector_instance: BasePlayerCollector | None = None
        self._season: str | None = None

    def navigate(self, collector: str, *args, **kwargs) -> None:
        """
        Navigate to the desired collector and initialize the collector class with the given arguments.

        Args:
            collector (str): The name of the collector to navigate to.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """

        logger.info("Navigator is initiated")

        self._collector = collector

        self._season = kwargs.get("season", None)
        if self._season is None:
            logger.error("Season is not provided")
            raise ValueError

        try:
            logger.info(f"Navigator is navigating to {collector}")
            module = importlib.import_module(f"fbref.fbref.collectors.{collector}")

            collectors = [
                obj
                for _, obj in module.__dict__.items()
                if isinstance(obj, BasePlayerCollector)
            ]

            if len(collectors) != 1:
                logger.error(f"Module {module} should contain exactly one class")
                raise ValueError

            self._collector_instance = collectors[0]
            self._collector_instance.season = self._season

        except ModuleNotFoundError:
            logger.exception(f"Module {collector} not found")
            raise ValueError
        except ImportError:
            logger.exception(f"Module {collector} not imported")
            raise ValueError

    def start(self) -> None:
        """
        Start the collection process and write the data to a file.
        """
        logger.info("Navigator is starting")
        if self._collector is None:
            logger.error("You should call navigate method first")
            raise ValueError

        self.feed.output_path = self.feed.output_path.format(
            season=self._season, name=self._collector
        )

        if self.download_deplay is not None:
            time.sleep(self.download_deplay)

        try:
            for record in self._collector_instance.collect():
                print(record)
                self.feed.write(record)
        except Exception as e:
            logger.exception(f"An error occurred: {e}")
            raise e
        finally:
            self.feed.close()
        logger.info("Navigator has finished")
