from dataclasses import dataclass

from movie import Movie


@dataclass
class Comedy(Movie):
    genre: str