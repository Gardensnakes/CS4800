from Steam import *

myfile = open("names", "r")
for line in myfile:
    google_steam(line)
myfile.close() 