# ZenithDS
# Lovesay: A script to display a quote from a loved one based on the day of the month

# Imports to make life easier 
from os.path import expanduser, exists
import shutil 
import textwrap as tr
from datetime import date
from rich import print
from lovesay.colors import colors

def get_file_path():

    home = expanduser('~')
    filePath = f"{home}/.config/lovesay/quotes"
    
    return filePath

def get_max_width():
    
    cols, rows = shutil.get_terminal_size()

    if cols // 2 != 0:
        cols -= 1
    
    return cols
    
def generate_quote(file_path):
    
    file_exists = exists(file_path)
   
    if file_exists:
        with open(file_path) as quotesFile:
            quotes = [ quote.strip() for quote in quotesFile ]
        
        maxWidth = get_max_width()

        today = date.today()
        todayDate = int(today.strftime("%d"))

        try:
            quotesList = tr.wrap(quotes[(todayDate - 1)], width = (maxWidth - 25))
        except ValueError:
            quotesList = None
        except IndexError:
            quotesList = ["No quote found for today, here's a hug :)"]
    else: 
        quotesList = None

    return quotesList

def format_quote(quotes_list, colorOne, fg):

    quoteList = ["", "", "", "", ""]
    
    if quotes_list is None:
        return quoteList    

    # A few logic checks right here to decide if the quote should be printed or not
    good_width = get_max_width() >= 52
    good_quote_length = len(quotes_list) <= 5

    if good_width and good_quote_length:
        for q in range(len(quotes_list)):
            quoteList[q] = f"{colorOne} [{fg}]{quotes_list[q].strip()}[/{fg}] {colorOne}"

    return quoteList

def main(quote, color_name):
    
    # Setting up the colors
    color_name = color_name.lower()
    if color_name in colors.keys():
        theme = colors[color_name]
    else:
        theme = colors['catppuccin']
    
    # Setting up the hearts 
    ONEHEART = f"[{theme['colorOne']}]\u2665[/{theme['colorOne']}]"
    TWOHEART = f"[{theme['colorTwo']}]\u2665[/{theme['colorTwo']}]"
    THREEHEART = f"[{theme['colorThree']}]\u2665[/{theme['colorThree']}]"
    FOURHEART = f"[{theme['colorFour']}]\u2665[/{theme['colorFour']}]"
    FIVEHEART = f"[{theme['colorFive']}]\u2665[/{theme['colorFive']}]"
    SIXHEART = f"[{theme['colorSix']}]\u2665[/{theme['colorSix']}]"

    # Setting up the things needed for the output
    if quote is None:
        raw_quote = generate_quote(get_file_path())
    else:
        raw_quote = [f"{quote}"]

    quoteList = format_quote(raw_quote, ONEHEART, theme['fg'])

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
