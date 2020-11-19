from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
from decimal import Decimal


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
	
	launcher = bs.find("div",{"class":"DRM_notice"})
	if launcher is not None:
		launcher = "Origin "
		print(launcher)
	else:
		launcher = "Steam"
		print(launcher)


	game_platform = bs.find("span",{"class":"platform_img win"})
	game_platform2 = bs.find("span",{"class":"platform_img mac"})
	release_date = bs.find("div",{"class":"date"}).get_text()
	print(release_date)
	game_details = bs.find("div",{"class":"glance_ctn_responsive_left"})
	count = 0;
	# for a in bs.find_all("div",{"class":"dev_row"}):
	# 	if count == 0:
	# 		print (a.get_text())
	# 		coutn = count + 1
	# 	if count == 1:
	# 		print (a.get_text())
	# 		count = count + 1
	for a in game_details.find_all('a', href=True):
		if count == 0:
			game_dev = a.get_text()
			print ("Dev: ", game_dev)
			count = count +1
		if count == 1:
			publisher = a.get_text()
			print ("Pub: ", publisher)
			count = count +1
	#print(game_dev)

	d = datetime.datetime.strptime(release_date, '%b %d, %Y')
	print(d.strftime('%Y-%m-%d'))


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
			final = (sub_area.get_text())
			print ("The Final Price is " + final.strip())
			final = Decimal(final.strip()[1:])

		else:
			sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
			sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
			final = sub_area.get_text()
			original = sub_area2.get_text()
			print("The Final Price is " + final.strip())
			print("The Original Price is " + original.strip())
			print("You save " )
			final = Decimal(final.strip()[1:])
			original = Decimal(original.strip()[1:])
			savings = orignal - final
			# saving = "$"+savings

	# Game must be on sale
	elif (sub_area is not None):
		final = (sub_area.get_text())
		print (final.strip())
		final = Decimal(final.strip()[1:])


	else:
		try:
			sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
			sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
			final = sub_area.get_text()
			original = sub_area2.get_text()
			print("The Final  Price is " +final.strip())
			print("The Original Price is " + original.strip())
			print("You save " )

			final = Decimal(final.strip()[1:])
			original = Decimal(original.strip()[1:])
			savings = orignal - final

		except:
			exit(0)
