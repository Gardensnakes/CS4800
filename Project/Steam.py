from urllib.request import urlopen
from bs4 import BeautifulSoup
from Class import *
from ImageDown import *

def google_steam(title):
	try: 
	    from googlesearch import search 
	except ImportError:  
	    print("No module named 'google' found") 
	  
	# to search 
	query = title +" steam store"
	for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
		first_link = j

	html = urlopen(first_link)
	bs = BeautifulSoup(html, 'html.parser')
	
	# Find game name and prints it
	game_name = bs.find("div", {"class":"apphub_AppName"})
	game_name = game_name.get_text()
	print(game_name)

	game_platform = bs.find("span",{"class":"platform_img win"})
	game_platform2 = bs.find("span",{"class":"platform_img mac"})

	if game_platform is not None:
		print("Supported on: Windows")

	if game_platform2 is not None:
		print("Supported on: Mac")

	# imgURL = resultRow.select('div.search_capsule img')[0].get('src')
	#imgURL = bs.find((lambda tag: tag.name == 'img' and tag.get('class') == ['game_header_image_full'])).get('src')
	#print(imgURL)
	#download(game_name,imgURL)

	# Looks in first section of steam section "add to cart"
	main = bs.find("div",{"class":"game_area_purchase_game"})
	sub_area = main.find("div",{"class":"game_purchase_price price"})

	# If it can't find a non-on-sale game price in the first section, check the next section
	if (sub_area is None):
		main = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['game_area_purchase_game_wrapper']))
		sub_area = main.find("div",{"class":"game_purchase_price price"})
	# if game is not on sale
		if sub_area is not None:
			result = (sub_area.get_text())
			print ("The Final Price is " + result.strip())
		else:
			sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
			sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
			discounted = sub_area.get_text()
			original = sub_area2.get_text()
			print("The Final Price is " + discounted.strip())
			print("The Original Price is " + original.strip())
			print("You save " )

	# Game must be on sale
	elif (sub_area is not None):
		result = (sub_area.get_text())
		print (result.strip())

	else:
		try:
			sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
			sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
			discounted = sub_area.get_text()
			original = sub_area2.get_text()
			print("The Final  Price is " +discounted.strip())
			print("The Original Price is " + original.strip())
			print("You save " )
		except:
			exit(0)

	