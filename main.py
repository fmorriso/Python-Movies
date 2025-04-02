import sys

from comedy import Comedy
from movie import Movie
from person import Person


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main():
    p = Person('Hansel', 'Bobbie')
    print(p)

    wonderful_life = Movie("It's a wonderful life", 1946, Person('Copra', 'Frank'))
    wonderful_life.add_cast_member(Person('Reed', 'Donna'))
    wonderful_life.add_cast_member(Person('Stewart', 'James'))
    print(wonderful_life)

    royalish = Comedy('Royal-ish', 2021, Person('Bobb', 'Roger'), 'Romantic Comedy')
    print(royalish)


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
