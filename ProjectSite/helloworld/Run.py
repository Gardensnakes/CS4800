from Steam import *
from Epic import *
from Origin import *
from re import sub
from decimal import Decimal
from Img_Search import *

# k=input("Enter game Title:  ") 
# google_steam(k)
# k=input("press enter to exit")

myfile = open("names.txt", "r")
for line in myfile:
	# try:
	# 	print("Gathering Steam Information on "+line)
	# 	google_steam(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	# try:
	# 	print("Gathering Origin Information on "+line)
	# 	google_origin(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	# try:
	# 	print("Gathering Epic Games Information on "+line)
	# 	google_epic(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	try:
		print(line,": Downloading Picture...")
		img_search(line)
		print("Success!\n")
	except:
		print("No Pic found\n")
myfile.close() 


