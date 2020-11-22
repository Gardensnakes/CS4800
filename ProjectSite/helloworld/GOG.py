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
# COUNT = 0
def google_gog(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +"gog.com"

    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j   

    driver = webdriver.Firefox(executable_path=PATH)
    if (first_link.find("gog.com") != -1):
        driver.get(first_link)
        driver.implicitly_wait(5)

    seller = 'GOG.com'
    name = driver.title.split(" on GOG.com", 1)[0]
   # name = name.replace('Buy ','')
    name = name.replace("™","")
    name = name.replace("®","")
    
    
    current_price = driver.find_element_by_xpath("//*[@class='product-actions-price__final-amount _price ng-binding']").text
    original_price = driver.find_element_by_xpath("//*[@class='product-actions-price__base-amount _price ng-binding']").text
    if (original_price != ""):
        current_price = Decimal(current_price.strip())
        original_price = Decimal(original_price.strip())
        current_price = (round(float(current_price),2))
        original_price = (round(float(original_price),2))
        savings_price = (original_price - current_price)
        print(current_price)
        print(original_price)
        print(savings_price)
        game = (name, seller,None, original_price, current_price, None, None, savings_price, None, None)
        insert_game(conn, game)
    else:
        current_price = Decimal(current_price.strip())
        current_price = (round(float(current_price),2))
        original_price = current_price
        savings_price = round(original_price - current_price)
        # print(current_price)
        # print(original_price)
        # print(round(savings_price))
        game = (name, seller,None, original_price, current_price, None, None, savings_price, None, None)
        insert_game(conn, game)

    print (get_game_info(conn,name))

    
    driver.quit()
#google_gog('Observer Redux')