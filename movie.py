from dataclasses import dataclass, InitVar
from typing import Optional

from person import Person


@dataclass
class Movie:
    title: str
    year: int
    director: Person
    # cast: Person = InitVar[Person]

    def __post_init__(self):
        self.cast: list[Person] = []

    def add_cast_member(self, member: Person) -> None:
        if self.cast is None:
            self.cast = [member]
        else:
            if member not in self.cast:
                self.cast.append(member)