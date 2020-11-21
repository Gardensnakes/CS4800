from urllib.request import urlopen
from bs4 import BeautifulSoup
# from ImageDown import *
import requests

def img_search(title):
	try: 
		from googlesearch import search 
	except ImportError:  
		print("No module named 'google' found") 
		  
	# to search 
	query = title +" game wikipedia"
	for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
		first_link = j

	html = urlopen(first_link)
	bs = BeautifulSoup(html, 'html.parser')

	main_area = bs.find("table",{"class":"infobox hproduct"})
	imgURL = main_area.find((lambda tag: tag.name == 'img')).get('src')
	# print(imgURL)
	# html = urlopen("https:" + imgURL[:-4])
	# print("https:" + imgURL[:-4])
	#print((imgURL.find((lambda tag: tag.name == 'img'))).get('src'))
	#print(imgURL)
	title = title.replace(':', '')
	file_path = "C:\\Users\\TJ\\Desktop\\Projectsite\\helloworld\\Images\\" + title[:-1]+".png"
	imgURL = imgURL.split(',')[0]
	work = "https:" + imgURL
	r = requests.get(work, stream=True)
	with open(file_path, 'wb') as beagle:
		for chunk in r.iter_content(chunk_size=1024):
			length = beagle.write(chunk)

	beagle.close()

