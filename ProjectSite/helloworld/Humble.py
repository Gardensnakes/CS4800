from selenium import webdriver
import time 
import datetime
from decimal import Decimal
from init_db import create_connection, create_table, insert_game
from extract_db import *
from selenium.webdriver.firefox.options import Options

PATH = "C:\\Users\\TJ\\Desktop\\testsite\\helloworld\\geckodriver.exe"

sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}

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

def google_humble(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" Humblebundle.com"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=PATH)

    if (first_link.find("humblebundle") != -1):
        driver.get(first_link, headers = headers)
        driver.implicitly_wait(5)
    try:
        driver.find_element_by_xpath("//select[@class='selection js-selection js-selection-year']/option[text()='1959']").click()
        driver.find_element_by_xpath("//*[@class='age-check-button submit-button js-submit-button']").click()
        time.sleep(3)
    except: 
        pass
    seller = "HumbleBundle.com"
    name = driver.title.split(" from the Humble Store", 1)[0]
    name = name.replace('Buy ','')
    name = name.replace("™","")
    name = name.replace("®","")
    try:
        original_price = driver.find_element_by_xpath("//*[@class='full-price']").text
        current_price = driver.find_element_by_xpath("//*[@class='current-price']").text
        original_price = round((float(original_price[1:])),2)
        current_price = (round(float(current_price[1:]),2))
        # print(original_price)
        # print(current_price)
        savings = original_price - current_price
        game = (name,seller, None, original_price, current_price, None, None, savings, None, None)
        insert_game(conn, game)
    except:
        try:
            discount = driver.find_element_by_xpath("//*[@class='js-discount-amount discount-amount']").text
            current_price = driver.find_element_by_xpath("//*[@class='current-price']").text
            current_price = Decimal(current_price[1:])
            if (discount.find('$')):
                discount = Decimal("." + discount[1:-5])
                original_price = (current_price/ (1-discount))
                original_price = round((float(original_price) + 0.01),2)
                current_price = (round(float(current_price),2))
                savings = original_price - current_price
                game = (name,seller, None, original_price, current_price, None, None, savings, None, None)
                insert_game(conn, game)  
        except:
            current_price = driver.find_element_by_xpath("//*[@class='current-price']").text
            current_price = (round(float(current_price[1:]),2))
            original_price = current_price
            savings = 0
            game = (name,seller, None, original_price, current_price, None, None, savings, None, None)
            insert_game(conn, game)


    print (get_game_info(conn,name))
    driver.quit()

# google_humble('Undertale')
# google_humble('KNIGHTS OF THE OLD REPUBLIC')
