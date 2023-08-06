"""
This file is the command line extra for the ASCIIcli module.
This module provides a command line tool for converting images to ASCII art.
"""

import argparse
import sys


try:
    from src.functions import convert_to_ascii
except ImportError:
    print('Error: Could not find function convert_to_ascii.')
    sys.exit()

try:
    from src.functions import listed_sets
except ImportError:
    print('Error: Could not find function convert_to_ascii.')
    sys.exit()

LISTS = len(listed_sets)

parser = argparse.ArgumentParser(
    prog='ASCIIcli',
    description='Converts an image to ASCII.',
    usage=argparse.SUPPRESS,
)


def main():
    """
    Parses the command line arguments for the ASCII art converter program.
    """

    parser.add_argument(
        '-percent',
        type=int,
        required=True,
        help='The percantage that will resize the output.'
    )

    parser.add_argument(
        '-set',
        type=int,
        choices=range(int(LISTS) + 1),
        default='1',
        help='Chooses character set to use.)'
    )

    parser.add_argument(
        '-gray',
        type=int,
        default=100,
        help='Gray value cut-off of line-art'
    )

    parser.add_argument(
        '-random',
        action='store_true',
        help='Scrambles characters in set'
    )

    parser.add_argument(
        '-invert',
        default=False,
        action='store_true',
        help='Output is inverted'
    )

    parser.add_argument(
        '-verbose',
        action='store_true',
        help='Displays developer information'
    )

    parser.add_argument(
        'path',
        metavar='path',
        type=str,
        help='The path to the image'
    )

    args = parser.parse_args()

    # call the functions from functions.py
    convert_to_ascii(args)


if __name__ == '__main__':
    main()
