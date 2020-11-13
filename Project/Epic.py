from urllib.request import urlopen
from bs4 import BeautifulSoup
from Class import *
from ImageDown import *
from selenium import webdriver
import time 

PATH = "C:\\Users\\TJ\\Desktop\\Project\\chromedriver.exe"

def google_epic(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" Epic Games Store"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    driver = webdriver.Chrome(PATH)
    driver.get(first_link)
    time.sleep(2)
    name = driver.title.split(" - ", 1)[0]
    game_developer = driver.find_element_by_xpath("//*[@data-component='MetaList']").text
    game_release = driver.find_element_by_xpath("//*[@data-component='Time']").text
    game_platform =driver.find_element_by_xpath("//*[@data-component='MetaPlatform']").text
    current = ""
    before_disc = ""
    
    try:
        price = driver.find_element_by_xpath("//*[@class='css-r6gfjb-PurchasePrice__priceContainer']").text
        if price[-4:] == "Free":
            before_disc = price.split("Free", 1)[0]
            current = "Free"
            # print (before_disc)
            # print (current)
            # print(price)
        else:
            print(forced_error)
    except:
        price = 0

    if price == 0:
        try:
            before_disc = driver.find_element_by_xpath("//*[@class='css-1kf4kf9-Price__discount']").text
            current = driver.find_element_by_xpath("//*[@class='css-ovezyj']").text
        except:
            try:
                before_disc = 0
                current = driver.find_element_by_xpath("//*[@class='css-8v8on4']").text
            except: 
                try:
                    before_disc = 0
                    current = driver.find_element_by_xpath("//*[@class='css-ovezyj']").text
                except:
                    exit(0)

    print(name)
    print(game_developer)
    print(game_release)
    print(game_platform)
    try: 
        print ("Before Discount: " + before_disc)
        print ("Current: "+ current)
    except:
        print ("Current: "+ current)

    print('\n')

    driver.quit()



