#!/usr/bin/env python3

# ZenithDS
# Lovesay: A script to display a quote from a loved one based on the day of the month
# Last edit Feb 18th, 2022

# Imports to make life easier 
from os.path import expanduser, exists
import os 
import textwrap as tr
from datetime import date
from rich import print
from lovesay.colors import colors

def get_file_path():

    home = expanduser('~')
    filePath = f"{home}/.config/lovesay/quotes"
    
    return filePath

def get_max_width():
    
    cols, rows = os.get_terminal_size()

    if cols // 2 != 0:
        cols -= 1
    
    return cols
    
def generate_quote(file_path):
    
    file_exists = exists(file_path)
   
    if file_exists:
        with open(file_path) as quotesFile:
            quotes = [ quote.rstrip() for quote in quotesFile ]
        
        maxWidth = get_max_width()

        today = date.today()
        todayDate = int(today.strftime("%d"))

        try:
            quotesList = tr.wrap(quotes[(todayDate - 1)], width = (maxWidth - 25))
        except ValueError:
            quotesList = ["", "", "", "", ""]
    else: 
        quotesList = ["", "", "", "", ""]

    return quotesList

def format_quote(quotes_list, red):

    filePath = get_file_path()
    quoteList = ["", "", "", "", ""]

    # A few logic checks right here to decide if the quote should be printed or not
    file_exists = exists(filePath)
    good_width = get_max_width() >= 52
    good_quote_length = len(generate_quote(filePath)) <= 5

    if file_exists and good_width and good_quote_length:
        for q in range(len(quotes_list)):
            quoteList[q] = f"{red} {quotes_list[q]} {red}"

    return quoteList

def main(color_name="catppuccin"):
    
    # Setting up the colors
    theme = colors[color_name]
    REDHEART = f"[{theme['red']}]\u2665[/{theme['red']}]"
    MAGENTAHEART = f"[{theme['magenta']}]\u2665[/{theme['magenta']}]"
    BLUEHEART = f"[{theme['blue']}]\u2665[/{theme['blue']}]"
    GREENHEART = f"[{theme['green']}]\u2665[/{theme['green']}]"
    ORANGEHEART = f"[{theme['orange']}]\u2665[/{theme['orange']}]"
    YELLOWHEART = f"[{theme['yellow']}]\u2665[/{theme['yellow']}]"

    # Setting up the things needed for the output
    filePath = get_file_path()
    quoteList = format_quote(generate_quote(filePath), REDHEART)

    bigHeart = f"   {REDHEART} {REDHEART}   {REDHEART} {REDHEART}   " \
               f"\n {MAGENTAHEART}     {MAGENTAHEART}     {MAGENTAHEART}      {quoteList[0]}" \
               f"\n {BLUEHEART}           {BLUEHEART}      {quoteList[1]}" \
               f"\n   {GREENHEART}       {GREENHEART}        {quoteList[2]}" \
               f"\n     {ORANGEHEART}   {ORANGEHEART}          {quoteList[3]}" \
               f"\n       {YELLOWHEART}            {quoteList[4]}"


    print(bigHeart)

if __name__ == "__main__":
    main()

# This marks the end of the script

# This was my first attempt at making something nice for myself and perhaps for others,
# I got tired of only using programming for boring old programming assignments so here we are. 
# I have a long way to go and I guess this is just the starting, I just hope that one day,
# when I look back this code, I'm actually proud of myself instead of being embarrassed. 
