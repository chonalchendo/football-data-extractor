import importlib
import json
import gzip

from .settings import Settings
from .collectors.base import BasePlayerCollector


class NavigatorRunner:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings 
        self._collector = None
        self._file = None

    def navigate(self, collector: str, *args, **kwargs) -> None:
        print(f"Navigator is running with {self.settings}")

        try:
            module = importlib.import_module(f"collectors.{collector}")
            classes = [obj for _, obj in module.__dict__.items() if isinstance(obj, type)]

            if len(classes) != 1:
                raise ValueError(f"Module {module} should contain exactly one class")

            collector_class = classes[0]

            if not issubclass(collector_class, BasePlayerCollector):
                raise ValueError(f"Class {collector_class} should be a subclass of Navigator")

            self._collector = collector_class(*args, **kwargs)

        except ModuleNotFoundError:
            raise ValueError(f"Module {collector} not found")
        except ImportError:
            raise ValueError(f"Module {collector} not imported")


    def start(self) -> None:
        print("Navigator is starting")
        if self._collector is None:
            raise ValueError("You should call navigate method first")

        try:
            for record in self._collector.collect():
                self._write_to_file(record)

        finally:
            if self._file:
                self._file.close()


    def _write_to_file(self, record: dict) -> None:
        
        feeds = self.settings.feeds
        if self.settings.overwrite:
            with gzip.open(feeds, 'wb') as f:
                pass

        self._file = gzip.open(feeds, "at")
        self._file.write(json.dumps(record))
        self._file.write("\n")


