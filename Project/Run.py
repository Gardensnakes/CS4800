from Steam import *
from Epic import *
from Origin import *
from Class import *
from re import sub
from decimal import Decimal
from ImageDown import *
#from Img_Search import *

# k=input("Enter game Title:  ") 
# google_steam(k)
# k=input("press enter to exit")

myfile = open("names.txt", "r")
for line in myfile:
	try:
    	google_steam(line)
    	print("")
    except:
    	pass
    try:
    	google_epic(line)(line)
    	print("")
    except:
    	pass
    try:
    	google_origin(line)
    	print("")
    except:
    	pass
   #img_search(line)
myfile.close() 

