from Steam import *
from Epic import *
from Origin import *
from re import sub
from decimal import Decimal
from Img_Search import *
from init_db import *
from GOG import *
from Humble import *
from extract_db import *



#connection  = create_connection("C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db")
# k=input("Enter game Title:  ") 
# google_steam(k)
# k=input("press enter to exit")

myfile = open("Names.txt", "r")
for line in myfile:
	# try:
	# 	print("Gathering Origin Information on "+line)
	# 	google_origin(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	# try:
	# 	print("Gathering Steam Information on "+line)
	# 	google_steam(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	# try:
	# 	print("Gathering Epic Games Information on "+line)
	# 	google_epic(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	# try:
	# 	print("Gathering Humble Bundle Information on "+line)
	# 	google_humble(line)
	# 	print("\n")
	# except:
	# 	print("No game found\n")
	# try:
	# 	print("Gathering GOG Information on "+line)
	# 	google_gog(line)
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




