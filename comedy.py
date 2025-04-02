from dataclasses import dataclass

from movie import Movie


@dataclass
class Comedy(Movie):
    genre: str


    def __repr__(self) -> str:
        return super().__repr__()
