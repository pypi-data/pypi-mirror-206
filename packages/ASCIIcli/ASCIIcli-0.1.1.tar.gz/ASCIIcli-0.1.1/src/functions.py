"""
This file is the functions for the ASCIIcli module.
This module provides a command line tool for converting images to ASCII art.
"""

# THINGSTODO:
# create a __notes__ file for every output
# create an exception for errors
# syntax highlighting for command

# https://en.wikipedia.org/wiki/Box_Drawing

# https://en.wikipedia.org/wiki/Geometric_Shapes_(Unicode_block)

# https://en.wikipedia.org/wiki/Braille_Patterns

# https://en.wikipedia.org/wiki/Mathematical_Operators_(Unicode_block)
#   https://en.wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-A
#   https://en.wikipedia.org/wiki/Supplemental_Mathematical_Operators
#   https://en.wikipedia.org/wiki/Miscellaneous_Mathematical_Symbols-B

# https://en.wikipedia.org/wiki/Enclosed_Alphanumerics

# https://en.wikipedia.org/wiki/Miscellaneous_Symbols
# https://en.wikipedia.org/wiki/Supplemental_Arrows-A
#   https://en.wikipedia.org/wiki/Miscellaneous_Symbols_and_Arrows
#   https://en.wikipedia.org/wiki/Dingbats_(Unicode_block)
#   https://en.wikipedia.org/wiki/Miscellaneous_Technical
#   https://en.wikipedia.org/wiki/Arrows_(Unicode_block)

import random
import os
import sys
import string
import tqdm as TQDM

try:
    import colorama
except ModuleNotFoundError:
    print(
        "Error: Could not find module colorama. Use `pip install colorama`. ",
    )
    sys.exit()

try:
    import PIL
    from PIL import Image
except ModuleNotFoundError:
    print(
        colorama.Fore.RED,
        colorama.Style.BRIGHT,
        "Error: Could not find module Pillow. Use `pip install pillow`. "
        + colorama.Style.RESET_ALL
    )
    sys.exit()

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    print(
        colorama.Fore.RED,
        colorama.Style.BRIGHT,
        "Error: Could not find module tqdm. Use `pip install tqdm`. "
        + colorama.Style.RESET_ALL
    )
    sys.exit()

# basic latin
charset_1 = list(string.ascii_uppercase)
charset_2 = list(string.ascii_lowercase)
charset_3 = list(string.digits)
charset_4 = [  # punctuation & typographical
    ',', ':', ':', '-', '″', '.', '&', '@', '^', '/', '*', '-', '=', '!',
    '¡', '?', '¡', '¿', '🙻', '|', '¦', '‖', '•', '·', '©', '℗', '®', '“',
    '”', "'", '"', '«', '»', '(', ')', '[', ']', '{', '}', '¶', '§', '†',
    '‡', '❧', '◊'
    ]
charset_5 = [  # math symbols
    '¤', 'µ', '¢', '¥', '£', '$', '%', '#', '№', 'º', 'ª', '%', '°', '+',
    '-', '÷', '×', '*', '/', '±', '¬', '~', '_', '^', '<', '>'
    ]

# block element characters
charset_6 = [  # assorted block element characters
    '░', '▒', '▓', '█'
    ]
charset_7 = [  # ascii square  characters
    '□', '▢', '◫', '◰', '◱', '◲', '◳', '◧', '◨', '◩', '◪', '◘', '▤',
    '▥', '▦', '▧', '▨', '▣', '▩', '■'
    ]

listed_sets = {
    1: charset_1,
    2: charset_2,
    3: charset_3,
    4: charset_4,
    5: charset_5,
    6: charset_6,
    7: charset_7,
    }


def get_char_set(set_choice):
    """
    Uses choice for character set by number and then returns the chosen set to.
    If 1 is chosen, character set A will be chosen and so on.
    """

    if set_choice in listed_sets:
        return listed_sets[set_choice]

    raise ValueError(
        colorama.Fore.RED,
        f"Error: Invalid set number {set_choice}"
        + colorama.Style.RESET_ALL)


def randomize(arg_set, arg_random):
    """
    Checks if the random variable is true, if so: randomize the character set.
    """

    char_set = get_char_set(arg_set)

    if arg_random is True:
        random.shuffle(char_set)
    return char_set


def find_dir(path):
    """
    Finds the directory file name and complete directory and sends to path
    """

    file_name = os.path.basename(path)
    directory = os.path.dirname(path)
    complete_path = f"{directory}/{file_name}"
    return complete_path


def get_gray_value(pixel):
    """
    Calculates the gray value of a pixel in the image.
    """

    return int(sum([pixel]) / 2)


def resize_height(image, percent):
    """
    Resizes the image to the given height while maintaining the aspect ratio.
    """

    # calculate the aspect ratio of the original image
    original_height = image.size[1]

    # calculate the new width and height based on the desired percentage ratio
    new_height = int(original_height * percent / 200)
    return new_height, original_height


def resize_width(image, percent):
    """
    Resizes the image to the given height while maintaining the aspect ratio.
    """

    # calculate the aspect ratio of the original image
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    # calculate the new width and height based on the desired percentage ratio
    new_height = int(original_height * percent / 100)
    new_width = int(new_height * aspect_ratio)
    return new_width, original_width


def gen_output(argument, complete_dir, finished_art):
    """
    Generates the output .txt file with the ending -ascii.txt.
    """

    # set path
    complete_path = find_dir(complete_dir)

    # generate output file into text
    file_name = argument.split(".")[0] + "-ascii.txt"
    output_file = os.path.join(complete_path, file_name)
    with open(output_file, "w", encoding="utf-8") as enc:
        enc.write(finished_art)

    # print to output file
    print(
        "Output Location:",
        colorama.Fore.LIGHTGREEN_EX + str(os.path.abspath(output_file))
        + colorama.Style.RESET_ALL
    )


def convert_to_ascii(args):
    """
    Converts the input image into an ASCII string.
    """

    # input is set
    char_set = get_char_set(args.set)

    # set the current working directory to the one of the input image
    os.chdir(os.path.dirname(args.path))

    # run other functions
    randomize(args.set, args.random)

    # set path
    complete_path = find_dir(args.path)

    # open and then resize image
    try:
        with Image.open(complete_path) as image:
            # envoke resize function
            used_height, old_height = resize_height(image, args.percent)
            used_width, old_width = resize_width(image, args.percent)
            if args.verbose:
                verb_args(used_height, used_width, old_height, old_width, args)

            image = image.resize((used_width, used_height))
    except FileNotFoundError:
        print(
            colorama.Fore.RED + "Error: Could not find file."
            + colorama.Style.RESET_ALL
        )
        sys.exit()

    # convert the image to ASCII art
    ascii_art = ""
    for y_val in tqdm(range(used_height), desc='Generating', colour='green'):
        for x_val in range(used_width):
            pixel = image.getpixel((x_val, y_val))
            gray_value = get_gray_value(pixel)
            if bool(args.invert):
                gray_value = 255 - gray_value
            if gray_value >= int(args.gray):
                ascii_char = " "
            else:
                index = int(gray_value / 10)
                ascii_char = char_set[index % len(char_set)]
            ascii_art += ascii_char
        ascii_art += "\n"

    gen_output(args.path, complete_path, ascii_art)


def verb_args(used_height, used_width, old_height, old_width, args):
    """
    Prints more information for development.
    """
    print(
        colorama.Fore.WHITE + "Original Height:",
        colorama.Fore.CYAN + str(old_height),
        colorama.Fore.WHITE + "New Height:",
        colorama.Fore.LIGHTCYAN_EX + str(used_height)
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "Original Width:",
        colorama.Fore.CYAN + str(old_width),
        colorama.Fore.WHITE + "New Width:",
        colorama.Fore.LIGHTCYAN_EX + str(used_width)
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "Colorama Version:", colorama.__version__
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "Pillow Version:", PIL.__version__
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "TQDM Version:", TQDM.__version__
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "Lines Used:",
        colorama.Fore.WHITE + str(used_height)
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "Chars-Per-Str:",
        colorama.Fore.WHITE + str(used_width)
        + colorama.Style.RESET_ALL
    )

    print(
        colorama.Fore.WHITE + "Set:",
        colorama.Fore.LIGHTBLUE_EX + str(args.set)
        + colorama.Style.RESET_ALL
    )

    if args.verbose is True:
        print(
            colorama.Fore.WHITE + 'Verbose:',
            colorama.Fore.GREEN + 'ON'
            + colorama.Style.RESET_ALL
        )
    else:
        print(
            colorama.Fore.WHITE + 'Verbose:',
            colorama.Fore.LIGHTRED_EX + 'OFF'
            + colorama.Style.RESET_ALL
        )

    if bool(args.random) is True:
        print(
            colorama.Fore.WHITE + 'Randomization:',
            colorama.Fore.GREEN + 'ON'
            + colorama.Style.RESET_ALL
        )
    else:
        print(
            colorama.Fore.WHITE + 'Randomization:',
            colorama.Fore.LIGHTRED_EX + 'OFF'
            + colorama.Style.RESET_ALL
        )

    if bool(args.invert) is True:
        print(
            colorama.Fore.WHITE + 'Invert:',
            colorama.Fore.GREEN + 'ON'
            + colorama.Style.RESET_ALL
        )
    else:
        print(
            colorama.Fore.WHITE + 'Invert:',
            colorama.Fore.LIGHTRED_EX + 'OFF'
            + colorama.Style.RESET_ALL
        )
