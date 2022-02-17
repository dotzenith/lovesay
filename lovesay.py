#!/usr/bin/env python3

# ZenithDS
# Lovesay: A script to display a quote from a loved one based on the day of the month
# Last edit Feb 16th, 2022

# Imports to make life easier 
from os.path import expanduser, exists
import os 
import textwrap as tr
from termcolor import colored
from datetime import date

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
    
    with open(file_path) as quotesFile:
        quotes = [ quote.rstrip() for quote in quotesFile ]

    maxWidth = get_max_width()

    today = date.today()
    todayDate = int(today.strftime("%d"))

    try:
        quotesList = tr.wrap(quotes[(todayDate - 1)], width = (maxWidth - 25))
    except ValueError:
        quotesList = ["", "", "", "", ""]

    return quotesList

def format_quote(quotes_list):

    filePath = get_file_path()
    quoteList = ["", "", "", "", ""]
    redHeart = colored("\u2665", "red")

    # A few logic checks right here to decide if the quote should be printed or not
    file_exists = exists(filePath)
    good_width = get_max_width() >= 52
    good_quote_length = len(generate_quote(filePath)) <= 5

    if file_exists and good_width and good_quote_length:
        for q in range(len(quotes_list)):
            quoteList[q] = f"{redHeart} {quotes_list[q]} {redHeart}"

    return quoteList

def main():

    # Setting up the things needed for the output
    filePath = get_file_path()
    quoteList = format_quote(generate_quote(filePath))
    
    # Making some hearts
    redHeart = colored("\u2665", "red")
    magentaHeart = colored("\u2665", "magenta")
    blueHeart = colored("\u2665", "blue")
    cyanHeart = colored("\u2665", "cyan")
    greenHeart = colored("\u2665", "green")
    yellowHeart = colored("\u2665", "yellow")

    bigHeart = f"   {redHeart} {redHeart}   {redHeart} {redHeart}   " \
               f"\n {magentaHeart}     {magentaHeart}     {magentaHeart}      {quoteList[0]}" \
               f"\n {blueHeart}           {blueHeart}      {quoteList[1]}" \
               f"\n   {cyanHeart}       {cyanHeart}        {quoteList[2]}" \
               f"\n     {greenHeart}   {greenHeart}          {quoteList[3]}" \
               f"\n       {yellowHeart}            {quoteList[4]}"


    print(bigHeart)

if __name__ == "__main__":
    main()

# This marks the end of the script

# This was my first attempt at making something nice for myself and perhaps for others,
# I got tired of only using programming for boring old programming assignments so here we are. 
# I have a long way to go and I guess this is just the starting, I just hope that one day,
# when I look back this code, I'm actually proud of myself instead of being embarrassed. 
