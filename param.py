from dataclasses import dataclass


@dataclass
class Video:
    path: str
    width: int
    height: int

    @property
    def is_portrait(self) -> bool:
        return self.height > self.width

    @property
    def is_landscape(self) -> bool:
        return self.width >= self.height

