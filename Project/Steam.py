from urllib.request import urlopen
from bs4 import BeautifulSoup

def google_steam(title):
	try: 
	    from googlesearch import search 
	except ImportError:  
	    print("No module named 'google' found") 
	  
	# to search 
	query = title +" steam"
	for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
		first_link = j

	# html = urlopen('https://store.steampowered.com/app/1222670/The_Sims_4/')
	html = urlopen(first_link)
	bs = BeautifulSoup(html, 'html.parser')
	
	# Find game name and prints it
	game_name = bs.find("div", {"class":"apphub_AppName"})
	print(game_name.get_text())
	# Looks in first section of steam section "add to cart"
	main = bs.find("div",{"class":"game_area_purchase_game"})
	sub_area = main.find("div",{"class":"game_purchase_price price"})

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
		sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
		sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
		discounted = sub_area.get_text()
		original = sub_area2.get_text()
		print("The Final  Price is " +discounted.strip())
		print("The Original Price is " + original.strip())
		print("You save " )

	