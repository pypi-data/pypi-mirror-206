"""
This file is the test area for the ASCIIcli module.
This module provides a command line tool for converting images to ASCII art.
"""

import unittest
import argparse
from src.functions import (randomize, get_char_set)


class Testing(unittest.TestCase):
    """
    The group of tests for ASCIIcli.
    """

    def test_randomize(self):
        """
        Randomizes the sets when the argument is True.
        """

        i = 1

        args = i, random = True

        char_set = get_char_set(args)
        randomized_set = randomize(args)

        with self.subTest(msg=f"Test {i}"):
            try:
                assert set(char_set) == set(randomized_set)
                i += 1

            except AssertionError:
                self.fail(
                    f"Set {i} is not valid:" +
                    {char_set} != {randomized_set}
                )

        with self.subTest(msg=f"Test {i}"):
            try:
                assert len(char_set) == len(randomized_set)
                i += 1

            except AssertionError:
                self.fail(
                    f"Set {i} is not valid:" +
                    {char_set} != {randomized_set}
                )

        with self.subTest(msg=f"Test {i}"):
            try:
                assert set(char_set) != randomized_set
                i += 1

            except AssertionError:
                self.fail(
                    f"Set {i} was not randomised: {char_set} =="
                    + {randomized_set})


if __name__ == '__main__':
    unittest.main()
