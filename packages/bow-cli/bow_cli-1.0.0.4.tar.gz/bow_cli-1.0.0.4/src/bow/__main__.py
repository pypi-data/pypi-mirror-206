import sys
from . import bow


def main():
    return bow(prog_name='bow', windows_expand_args=False)


if __name__ == '__main__':
    sys.exit(main())