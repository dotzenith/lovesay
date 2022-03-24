# ZenithDS
# Lovesay: A script to display a quote from a loved one based on the day of the month

# Imports to make life easier 
from os.path import expanduser, exists
import shutil 
import textwrap as tr
from datetime import date
from lovesay.colors import colors

def get_file_path():

    '''
    get_file_path() -> String

    Returns the absolute path to where the quotes file should be stored

    :params - None
    '''

    home = expanduser('~')
    filePath = f"{home}/.config/lovesay/quotes"
    
    return filePath

def get_max_width():
    
    '''
    get_file_path() -> int

    Returns the current width of the terminal window

    :params - None
    '''
    
    cols, rows = shutil.get_terminal_size()

    return cols
    
def generate_quote(from_file = True, file_path=get_file_path(), quote=""):

    '''
    generate_quote(file_path) -> List of Strings

    Returns the quote for the current day as a list of strings 
    given the path to the quotes file. 

    The quote is broken into smaller segments 
    based on the width of the terminal window and stored in a list 
    
    :param from_file - Toggle between generating quote from a file or a given string
    :param file_path - The absolute path to the quotes file 
    :param quote - A given quote if from_file is False 
    '''

    file_exists = exists(file_path)
    maxWidth = get_max_width()

    if from_file and file_exists:
        with open(file_path) as quotesFile:
            quotes = [ quote.strip() for quote in quotesFile ]    

        today = date.today()
        todayDate = int(today.strftime("%d"))

        try:
            quotesList = tr.wrap(quotes[(todayDate - 1)], width = (maxWidth - 25))
        except ValueError:
            quotesList = None
        except IndexError:
            quotesList = ["No quote found for today, here's a hug :)"]
    elif not(from_file): 
        try:
            quotesList = tr.wrap(quote, width = (maxWidth - 25))
        except ValueError:
            quotesList = None
    else:
        quotesList = None

    return quotesList

def format_quote(quotes_list, heartOne, fg):

    '''
    format_quote(quotes_list, heartOne, fg) -> List of Strings

    Formats the quote with hearts around it and a specified foreground color 

    :param quotes_list - A list of strings generated from generate_quote
    :param heartOne - The heart character which will be wrapped around the quote
    :param fg - A the foreground color for the quote 
    '''
    
    quoteList = ["", "", "", "", ""]
    
    if quotes_list is None:
        return quoteList    

    # A few logic checks right here to decide if the quote should be printed or not
    good_width = get_max_width() >= 52
    good_quote_length = len(quotes_list) <= 5

    if good_width and good_quote_length:
        for q in range(len(quotes_list)):
            quoteList[q] = f"{heartOne} {fg}{quotes_list[q].strip()}\033[0m {heartOne}"

    return quoteList

def main(quote, color_name):

    '''
    main(quote, color_name) -> None

    The main function to print out the heart and the quote

    :param quote - A quote if the user wants to something arbitrary
    :param color_name - The name of the color scheme to be used for the output 
    '''
    
    # Setting up the colors
    color_name = color_name.lower()
    if color_name in colors.keys():
        theme = colors[color_name]
    else:
        theme = colors['catppuccin']

    # Setting up the hearts 
    ONEHEART = f"\033[38;2;{theme['colorOne']['R']};{theme['colorOne']['G']};{theme['colorOne']['B']}m\u2665\033[0m"
    TWOHEART = f"\033[38;2;{theme['colorTwo']['R']};{theme['colorTwo']['G']};{theme['colorTwo']['B']}m\u2665\033[0m"
    THREEHEART = f"\033[38;2;{theme['colorThree']['R']};{theme['colorThree']['G']};{theme['colorThree']['B']}m\u2665\033[0m"
    FOURHEART = f"\033[38;2;{theme['colorFour']['R']};{theme['colorFour']['G']};{theme['colorFour']['B']}m\u2665\033[0m"
    FIVEHEART = f"\033[38;2;{theme['colorFive']['R']};{theme['colorFive']['G']};{theme['colorFive']['B']}m\u2665\033[0m"
    SIXHEART = f"\033[38;2;{theme['colorSix']['R']};{theme['colorSix']['G']};{theme['colorSix']['B']}m\u2665\033[0m"

    # Setting up the things needed for the output
    if quote is None:
        raw_quote = generate_quote(from_file=True, file_path=get_file_path())
    else:
        raw_quote = generate_quote(from_file=False, quote=quote)

    quoteList = format_quote(raw_quote, ONEHEART, f"\033[38;2;{theme['fg']['R']};{theme['fg']['G']};{theme['fg']['B']}m")

    bigHeart = f"   {ONEHEART} {ONEHEART}   {ONEHEART} {ONEHEART}   " \
               f"\n {TWOHEART}     {TWOHEART}     {TWOHEART}      {quoteList[0]}" \
               f"\n {THREEHEART}           {THREEHEART}      {quoteList[1]}" \
               f"\n   {FOURHEART}       {FOURHEART}        {quoteList[2]}" \
               f"\n     {FIVEHEART}   {FIVEHEART}          {quoteList[3]}" \
               f"\n       {SIXHEART}            {quoteList[4]}"


    print(bigHeart)

if __name__ == "__main__":
    main("", 'catppuccin')

# This marks the end of the script

# This was my first attempt at making something nice for myself and perhaps for others,
# I got tired of only using programming for boring old programming assignments so here we are. 
# I have a long way to go and I guess this is just the starting, I just hope that one day,
# when I look back this code, I'm actually proud of myself instead of being embarrassed. 

