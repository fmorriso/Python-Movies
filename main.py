import sys
from person import Person


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main():
    p = Person('Hansel', 'Bobbie')
    print(p)

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()
