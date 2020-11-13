from urllib.request import urlopen
from bs4 import BeautifulSoup
from ImageDown import *

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

	imgURL = (bs.find((lambda tag: tag.name == 'img'))).get('srcset')
	html = urlopen(imgURL[:-4])
	imgURL = (bs.find((lambda tag: tag.name == 'img'))).get('src')

	#download(title, imgURL)

#download(title, imgURL)
#img_search('Squadrons')