# Dotzenith
# Lovesay: A script to display a quote from a loved one based on the day of the month

import textwrap as tr
from datetime import date

from os import getenv
from os.path import exists, expanduser
from typing import Optional

from kolorz.kolor import get_all_colorschemes, make_kolorz


def get_file_path() -> str:
    """
    Returns the absolute path to where the quotes file should be stored

    :params - None
    """

    lovesay_path = getenv("LOVESAY_PATH", "~/.config/lovesay/quotes")

    return expanduser(lovesay_path)


def generate_quote(
    max_width: int,
    from_file: bool = True,
    file_path: str = get_file_path(),
    quote: str = "",
) -> Optional[list[str]]:
    """
    Returns the quote for the current day as a list of strings
    given the path to the quotes file.

    The quote is broken into smaller segments
    based on the width of the terminal window and stored in a list

    :param from_file - Toggle between generating quote from a file or a given string
    :param file_path - The absolute path to the quotes file
    :param quote - A given quote if from_file is False
    """

    file_exists = exists(file_path)

    if from_file and file_exists:
        with open(file_path) as quotesFile:
            quotes = [quote.strip() for quote in quotesFile]

        today = date.today()
        todayDate = int(today.strftime("%d"))

        try:
            quotesList = tr.wrap(quotes[(todayDate - 1)], width=(max_width - 25))
        except ValueError:
            quotesList = None
        except IndexError:
            quotesList = ["No quote found for today, here's a hug :)"]
    elif not (from_file):
        try:
            quotesList = tr.wrap(quote, width=(max_width - 25))
        except ValueError:
            quotesList = None
    else:
        quotesList = None

    return quotesList


def format_quote(
    quotes_list: Optional[list[str]], heartOne: str, fg: str, max_width: int
) -> list[str]:
    """
    Formats the quote with hearts around it and a specified foreground color

    :param quotes_list - A list of strings generated from generate_quote
    :param heartOne - The heart character which will be wrapped around the quote
    :param fg - A the foreground color for the quote
    """

    quoteList = ["", "", "", "", ""]

    if quotes_list is None:
        return quoteList

    # Check terminal width to decide if the quote should be printed
    good_width = max_width >= 52

    if good_width:
        for index, _ in enumerate(quotes_list):
            try:
                quoteList[
                    index
                ] = f"{heartOne} {fg}{quotes_list[index].strip()}\033[0m {heartOne}"
            except IndexError:
                # Append if index goes out of bounds
                quoteList.append(
                    f"{heartOne} {fg}{quotes_list[index].strip()}\033[0m {heartOne}"
                )

    return quoteList


def main(quote: Optional[str], color_name: str, max_width: int) -> None:

    """
    The main function to print out the heart and the quote

    :param quote - A quote if the user wants to something arbitrary
    :param color_name - The name of the color scheme to be used for the output
    """

    # Setting up the colors
    color_name = color_name.lower()
    if color_name in get_all_colorschemes():
        theme = make_kolorz(color_name)
    else:
        theme = make_kolorz("catppuccin mocha")

    # Setting up the hearts
    ONEHEART = f"{theme.red}\uf004{theme.end}"
    TWOHEART = f"{theme.purple}\uf004{theme.end}"
    THREEHEART = f"{theme.blue}\uf004{theme.end}"
    FOURHEART = f"{theme.green}\uf004{theme.end}"
    FIVEHEART = f"{theme.orange}\uf004{theme.end}"
    SIXHEART = f"{theme.yellow}\uf004{theme.end}"

    # Setting up the things needed for the output
    if quote is None:
        raw_quote = generate_quote(max_width, from_file=True, file_path=get_file_path())
    else:
        raw_quote = generate_quote(max_width, from_file=False, quote=quote)

    quoteList = format_quote(raw_quote, ONEHEART, str(theme.white), max_width)

    bigHeart = (
        f"   {ONEHEART} {ONEHEART}   {ONEHEART} {ONEHEART}   "
        f"\n {TWOHEART}     {TWOHEART}     {TWOHEART}      {quoteList[0]}"
        f"\n {THREEHEART}           {THREEHEART}      {quoteList[1]}"
        f"\n   {FOURHEART}       {FOURHEART}        {quoteList[2]}"
        f"\n     {FIVEHEART}   {FIVEHEART}          {quoteList[3]}"
        f"\n       {SIXHEART}            {quoteList[4]}"
    )

    # If quoteList spans more than five lines, concatenate bigHeart with remaining lines
    if len(quoteList) > 5:
        for line in quoteList[5:]:
            bigHeart += f"\n                    {line}"

    print(bigHeart)


if __name__ == "__main__":
    main("", "catppuccin mocha", 80)

# This marks the end of the script

# This was my first attempt at making something nice for myself and perhaps for others,
# I got tired of only using programming for boring old programming assignments so here we are.
# I have a long way to go and I guess this is just the starting, I just hope that one day,
# when I look back this code, I'm actually proud of myself instead of being embarrassed.
