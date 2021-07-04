# ZenithDS
# Lovesay: A script to display a quote from a loved one based on the day of the month
# Last edit July 2nd, 2021

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
filePath = "{}/.config/quotes".format(home)

# opening the quotes file, storing each quote in a list, and then closing the file
with open(filePath) as quotesFile:
    quotes = [ quote.rstrip() for quote in quotesFile ]

# Getting the number of columns and rows to make sure the quoute looks presentable on most terminal window sizes
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

finalQuote = tr.wrap(quotes[(todayDate - 1)], width = (maxWidth - 25))


# Printing out the heart and the quote side to side turned out to be harder than I thought it would be.
# I couldn't use a neat little for loop, atleast to my knwoledge. 
# So, the lines of code follwing this comment block are likely an absolute mess, but they print out a beautiful heart
# I promise.


# Prints out the first line of the heart
print(colored(("   {} {}   {} {}   ".format("\u2665","\u2665","\u2665","\u2665")), "red"), end='')

# Prints out the second line of the heart as well as the first line of the quote
# This first one doesn't have a an error catcher since all quotes have atleast one line
print(colored(("\n {}     {}     {}".format("\u2665","\u2665","\u2665")), "magenta"), end='')
print("      {} {} {}".format((colored("\u2665", "red")), (finalQuote[0]), (colored("\u2665", "red"))), end='')

# All the lines of the heart and the quote after this point have error catchers because 
# I wasn't exactly sure how else to make sure that all lines of the qoute were printed out. 
# The program simply tries to print out the next line in the list, and if there is none, it prints nothing. 

# This particular segment is for the third line
print(colored(("\n {}           {}".format("\u2665","\u2665")), "blue"), end='')
try:
    print("      {} {} {}".format((colored("\u2665", "red")), (finalQuote[1]), (colored("\u2665", "red"))), end='')
except IndexError:
    print('', end='')

# This segment is for the fourth line
print(colored(("\n   {}       {}   ".format("\u2665","\u2665")), "cyan"), end='')
try:
    print("     {} {} {}".format((colored("\u2665", "red")), (finalQuote[2]), (colored("\u2665", "red"))), end='')
except IndexError:
    print('', end='')

# This segment is for the fifth line
print(colored(("\n     {}   {}     ".format("\u2665","\u2665")), "green"), end='')
try:
    print("     {} {} {}".format((colored("\u2665", "red")), (finalQuote[3]), (colored("\u2665", "red"))), end='')
except IndexError:
    print('', end='')

# This segment is for the sixth line
print(colored(("\n       {}       ".format("\u2665")), "yellow"), end='')
try:
    print("     {} {} {}".format((colored("\u2665", "red")), (finalQuote[4]), (colored("\u2665", "red"))), end='')
except IndexError:
    print('')

# This marks the end of the script

# This was my first attempt at making something nice for myself and perhaps for others,
# I got tired of only using programming for boring old programming assignments so here we are. 
# I have a long way to go and I guess this is just the starting, I just hope that one day,
# when I look back this code, I'm actually proud of myself instead of being embarrassed. 
