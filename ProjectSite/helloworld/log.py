from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
from decimal import Decimal
from init_db import create_connection, create_table, insert_game
from extract_db import *

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
def google_log(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = "isthereanydeal.com" + title
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j
    first_link = first_link[:-6] + "/history/"

    if (first_link.find("isthereanydeal.com") != -1):
        html = urlopen(first_link)
        bs = BeautifulSoup(html, 'html.parser')


    name = bs.find("h1", {"id":"gameTitle"}).get_text()
    log_section = bs.find_all("div", {"class":"lg2 game"})
    for i in log_section:
        title = i.find("span", {"class":"shopTitle"}).get_text()
        if (title == "Steam") or (title == "Origin") or (title == "Epic Game Store") or (title== "Humble Store") or (title == "GOG"):
            date_scraped = i.find("span", {"class":"lg2__time-rel"}).get_text()
            date_scraped = date_scraped[0:16]
            if title == "Humble Store":
                title = "Humblebundle.com"
            elif title == "Epic Game Store":
                title = "EpicGames.com"
            else:
                title = title+ ".com"
            original_price = Decimal(i.find("span", {"class":"lg2__price"}).get_text()[1:])
            current_price = Decimal(i.find("span", {"class":"lg2__price--new"}).get_text()[1:])
            savings_price = round(float(original_price-current_price),2)
            original_price = float(original_price)
            current_price = float(current_price)
            game = (name, title, None, original_price, current_price, None, None, savings_price, None, None, date_scraped)
            insert_game(conn, game)


    