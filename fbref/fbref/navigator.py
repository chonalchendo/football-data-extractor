import gzip
import importlib
import json
from gzip import GzipFile
from pathlib import Path
from typing import TextIO

from rich import print

from .collectors.base import BasePlayerCollector
from .settings import Settings
from .utils.logger import get_logger

logger = get_logger(__name__)


class NavigatorRunner:
    """
    NavigatorRunner is a class that is responsible for running the fbref data collectors -
    analogous to a spider in a web scraping framework. It is responsible for navigating to the
    desired collector, starting the collection process, and writing the data to a file.
    """

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._collector: str | None = None
        self._collector_instance: BasePlayerCollector | None = None
        self._file: GzipFile | TextIO | None = None
        self._output_path: str | None = None
        self._season: str | None = None

    def navigate(self, collector: str, *args, **kwargs) -> None:
        """
        Navigate to the desired collector and initialize the collector class with the given arguments.

        Args:
            collector (str): The name of the collector to navigate to.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """

        logger.info(f"Navigator is running with {self.settings}")

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

        feeds = self.settings.FEEDS

        self._output_path = feeds["path"].format(
            season=self._season, name=self._collector
        )

        if not Path(self._output_path).parent.exists():
            logger.info(f"Creating directory {Path(self._output_path).parent}")
            Path(self._output_path).parent.mkdir(parents=True, exist_ok=True)

        if feeds["overwrite"]:
            logger.info(f"Overwriting file {self._output_path}")
            with gzip.open(self._output_path, "wb") as f:
                pass

        try:
            for record in self._collector_instance.collect():
                print(record)
                self._write_to_file(record)
        except Exception as e:
            logger.exception(f"An error occurred: {e}")
            raise e
        finally:
            if self._file:
                logger.info(f"Closing file {self._output_path}")
                self._file.close()

        logger.info("Navigator has finished")

    def _write_to_file(self, record: dict) -> None:
        """
        Write the record to the file.

        Args:
            record (dict): The record to write to the file.
        """
        self._file = gzip.open(self._output_path, "at")
        self._file.write(json.dumps(record))
        self._file.write("\n")
