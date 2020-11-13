from ImageDown import *
from selenium import webdriver
import time 

PATH = "C:\\Users\\TJ\\Desktop\\Project\\chromedriver.exe"

def google_origin(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" Origin.com"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    driver = webdriver.Chrome(PATH)
    driver.get(first_link)
    time.sleep(4)
    name = driver.title.split("for PC", 1)[0]
    onwindow = True
    onmac = False
    developer = driver.find_element_by_xpath("//*[@ng-bind-html='::developerLink.label']").text
    platform = driver.find_element_by_xpath("//*[@class='otkicon otkicon-windows']")
    platform2 = ""
    try:
    	platform2 = driver.find_element_by_xpath("//*[@class='otkicon otkicon-apple']")
    except:
    	pass

    try:
    	price = driver.find_element_by_xpath("//*[@class='origin-white-space-nowrap']").text
    except:
    	try:
    		driver.find_element_by_xpath("//*[@class='otkbtn otkbtn-primary otkbtn-primary-btn']").click()
    		time.sleep(2)
    		price = driver.find_element_by_xpath("//*[@class='origin-white-space-nowrap']").text
    	except:
    		print("Nopeplatform")
    		exit(0)

    
    if platform != "" and platform2 != "":
   		onmac = True

    print(name)
    print(price)
    print(developer)
    # print(current)
    #driver.quit()
    #https://www.origin.com/usa/en-us/store/the-sims/the-sims-4/interstitial
    #https://www.origin.com/usa/en-us/store/the-sims/the-sims-4/interstitial
    driver.quit()

google_origin('Sims 4')