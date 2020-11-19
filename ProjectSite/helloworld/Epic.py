from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time 
import datetime
from decimal import Decimal

PATH = "C:\\Users\\TJ\\Desktop\\testsite\\helloworld\\chromedriver.exe"

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
    launcher = "Epic Games"
    game_release = driver.find_element_by_xpath("//*[@data-component='Time']").text
    game_platform =driver.find_element_by_xpath("//*[@data-component='MetaPlatform']").text
    d = datetime.datetime.strptime(game_release, '%b %d, %Y')
    game_release = d.strftime('%Y-%m-%d')
    final = ""


    
    try:
        price = driver.find_element_by_xpath("//*[@class='css-r6gfjb-PurchasePrice__priceContainer']").text
        if price[-4:] == "Free":
            original = price.split("Free", 1)[0]
            final = Decimal('0')
            # print (original)
            # print (final)
            # print(price)
        else:
            print(forced_error)
    except:
        price = 0

    if price == 0:
        try:
            original = driver.find_element_by_xpath("//*[@class='css-1kf4kf9-Price__discount']").text
            final = driver.find_element_by_xpath("//*[@class='css-ovezyj']").text
            final = Decimal(final.strip()[1:])
            original = Decimal(original.strip()[1:])
            savings = orignal - final

        except:
            try:
                final = driver.find_element_by_xpath("//*[@class='css-8v8on4']").text
                final = Decimal(final.strip()[1:])
            except: 
                try:
                    final = driver.find_element_by_xpath("//*[@class='css-ovezyj']").text
                    final = Decimal(final.strip()[1:])
                except:
                    exit(0)

    print(name)
    print(game_developer)
    print(game_release)
    print(game_platform)
    try: 
        print ("Before Discount: ",original)
        print ("final: ",final)
    except:
        print ("final: ",final)

    print('\n')

    driver.quit()



