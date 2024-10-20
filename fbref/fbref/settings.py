from dataclasses import dataclass


@dataclass
class Settings:
    def setdict(self, settings: dict) -> None:
        for key, value in settings.items():
            self.set(key, value)

    def set(self, key: str, value: str) -> None:
        setattr(self, key, value)
