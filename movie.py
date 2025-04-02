from dataclasses import dataclass, asdict

from person import Person


@dataclass
class Movie:
    title: str
    year: int
    director: Person
    # cast is optional, so we initialize it in the special __post_init__ method

    def __post_init__(self):
        self.cast: list[Person] = []

    def __repr__(self) -> str:
        result = asdict(self)
        # augment with cast list
        key = 'cast'
        result[key] = self.cast
        # convert dictionary to nicer looking output string
        movie = 'Movie('
        for k, v in result.items():
            movie += f'{k}={v}, '

        movie += ')'
        return movie

    def add_cast_member(self, member: Person) -> None:
        if member not in self.cast:
            self.cast.append(member)
