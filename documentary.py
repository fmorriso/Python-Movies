from dataclasses import dataclass

from movie import Movie
from person import Person


@dataclass
class Documentary(Movie):
    narrator: Person
