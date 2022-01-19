# ZenithDS
# Lovesay: A script to display a quote from a loved one based on the day of the month
# Last edit July 16th, 2021

# Importing the expanduser function which will be used to get the home directory
from os.path import expanduser

# Importing the os library to make a few things easier later on
import os 

# Importing textwrap, which will be used to display information nicely
import textwrap as tr

# Importing colored function from termcolor to output color to the terminal
from termcolor import colored

# Importing date function from datetime to help with quote assignment based on the day
from datetime import date

# getting the home directory to read the quotes file from
home = expanduser('~')

# setting the path for the quotes files
# The default is ~/.config/quotes
filePath = "{}/.config/lovesay/quotes".format(home)

# opening the quotes file, storing each quote in a list, and then closing the file
with open(filePath) as quotesFile:
    quotes = [ quote.rstrip() for quote in quotesFile ]

# Getting the number of columns and rows to make sure the quote looks presentable on most terminal window sizes
cols, rows = os.get_terminal_size()

# Making a max width variable to avoid confusion later on 
maxWidth = cols

# getting a nice even number for the max width to make things easier to work with
if maxWidth // 2 != 0:
    maxWidth -= 1

# The original intention of this script was to display a different quote for every day of the month
# This segment simply assigns a quote based on the date. 

today = date.today()
todayDate = int(today.strftime("%d"))

quotesList = tr.wrap(quotes[(todayDate - 1)], width = (maxWidth - 25))

# Making some hearts
redHeart = colored("\u2665", "red")
magentaHeart = colored("\u2665", "magenta")
blueHeart = colored("\u2665", "blue")
cyanHeart = colored("\u2665", "cyan")
greenHeart = colored("\u2665", "green")
yellowHeart = colored("\u2665", "yellow")

# The intended function is to print at most, five lines, so I made a list with five strings,
# that will be filled in accordingly. 

linesList = ["", "", "", "", ""]

for q in range(len(quotesList)):
    linesList[q] = f"{redHeart} {quotesList[q]} {redHeart}"

# Printing out the big heart with the quote
bigHeart = f"   {redHeart} {redHeart}   {redHeart} {redHeart}   " \
           f"\n {magentaHeart}     {magentaHeart}     {magentaHeart}      {linesList[0]}" \
           f"\n {blueHeart}           {blueHeart}      {linesList[1]}" \
           f"\n   {cyanHeart}       {cyanHeart}        {linesList[2]}" \
           f"\n     {greenHeart}   {greenHeart}          {linesList[3]}" \
           f"\n       {yellowHeart}            {linesList[4]}"

print(bigHeart)

# This marks the end of the script

# This was my first attempt at making something nice for myself and perhaps for others,
# I got tired of only using programming for boring old programming assignments so here we are. 
# I have a long way to go and I guess this is just the starting, I just hope that one day,
# when I look back this code, I'm actually proud of myself instead of being embarrassed. 

