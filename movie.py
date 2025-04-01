from dataclasses import dataclass
from typing import Optional

from person import Person


@dataclass
class Movie:
    title: str
    year: int
    director: Person
    cast: Optional[list[Person]] = None

    def add_cast_member(self, member: Person) -> None:
        if member not in self.cast:
            self.cast.append(member)