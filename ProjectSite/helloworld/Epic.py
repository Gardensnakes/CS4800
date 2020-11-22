from selenium import webdriver
import time 
import datetime
from decimal import Decimal
from init_db import create_connection, create_table, insert_game
from extract_db import *

PATH = "C:\\Users\\TJ\\Desktop\\testsite\\helloworld\\geckodriver.exe"

sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
conn = create_connection(sql_path)
game_table = """ CREATE TABLE IF NOT EXISTS game_info (
                                            Name TEXT,
                                            Seller TEXT,
                                            game_release DATETIME,
                                            original_price REAL,
                                            current_price REAL,
                                            MacWin TEXT,
                                            launcher TEXT,
                                            savings_price REAL,
                                            developer TEXT,
                                            publisher TEXT,
                                            Date_scraped DATETIME,
                                            PRIMARY KEY(Name,Seller,Date_scraped)            
                                        ); """

if conn is not None:
        create_table(conn, game_table) 

def google_epic(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" Epic Games Store"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    driver = webdriver.Firefox(executable_path=PATH)
    if (first_link.find("epicgames.com") != -1):
        driver.get(first_link)
        driver.implicitly_wait(10)
    name = driver.title.split(" - ", 1)[0]
    descr = driver.find_elements_by_xpath("//*[@data-component='MetaList']")
    count = 0
    for i in descr:
        if (count == 1):
            developer = i.text
        if (count == 3):
            publisher = i.text
        count = count + 1


    launcher = "Epic Games"
    game_release = driver.find_element_by_xpath("//*[@data-component='Time']").text
    MacWin =driver.find_element_by_xpath("//*[@data-component='MetaPlatform']").text
    d = datetime.datetime.strptime(game_release, '%b %d, %Y')
    game_release = d.strftime('%Y-%m-%d')
    current_price = ""
    Seller = "EpicGames.com"

    try:
        price = driver.find_element_by_xpath("//*[@class='css-r6gfjb-PurchasePrice__priceContainer']").text
        if price[-4:] == "Free":
            original_price = price.split("Free", 1)[0]

        else:
            print(forced_error)
    except:
        price = 0

    if price == 0:
        try:
            original_price = driver.find_element_by_xpath("//*[@class='css-1kf4kf9-Price__discount']").text
            current_price = driver.find_element_by_xpath("//*[@class='css-ovezyj']").text
            current_price = Decimal(current_price.strip()[1:])
            original_price = Decimal(original_price.strip()[1:])
            current_price = (round(float(current_price),2))
            original_price = (round(float(original_price),2))
            savings_price = original_price - current_price

        except:
            try:
                current_price = driver.find_element_by_xpath("//*[@class='css-8v8on4']").text
                current_price = Decimal(current_price.strip()[1:])
                current_price = (round(float(current_price),2))
                original_price = current_price
                savings_price = original_price - current_price

            except: 
                try:
                    current_price = driver.find_element_by_xpath("//*[@class='css-ovezyj']").text
                    current_price = Decimal(current_price.strip()[1:])
                    current_price = (round(float(current_price),2))
                    original_price = current_price
                    savings_price = original_price - current_price
                except:
                    exit(0)

    print(name)
    developer = developer.replace("Developer","")
    developer = developer.strip()
    print(game_release)
    MacWin = MacWin.replace("Platform","")
    MacWin = MacWin.replace("\n","")
    if (MacWin == "WindowsMac"):
        MacWin = "Windows, Macintosh"
    else:
        MacWin = "Windows"
    print(MacWin)

    game = (name, Seller,game_release, original_price, current_price, MacWin, launcher, savings_price, developer, publisher)
    insert_game(conn, game)
    print (get_game_info(conn,name))
    print('\n')

    driver.quit()



