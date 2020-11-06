from Steam import *
from Class import *
from re import sub
from decimal import Decimal

# k=input("Enter game Title:  ") 
# google_steam(k)
# k=input("press enter to exit")

myfile = open("names.txt", "r")
for line in myfile:
    google_steam(line)
    print("")
myfile.close() 
