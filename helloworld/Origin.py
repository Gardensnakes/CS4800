from selenium import webdriver
import time 
import datetime
from decimal import Decimal
from init_db import create_connection, create_table, insert_game
from extract_db import *
from selenium.webdriver.firefox.options import Options

PATH = "C:\\Users\\administrator\\Desktop\\testsite\\helloworld\\geckodriver.exe"

sql_path = r"C:\\Users\\administrator\\Desktop\\testsite\\helloworld\\Games.db"
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

def google_origin(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" Origin.com"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    options = Options()
    # options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=PATH)
    driver = webdriver.Firefox(executable_path=PATH)
    MacWin = "Windows"

    if (first_link.find("origin.com") != -1):
        driver.get(first_link)
        time.sleep(10)
    name = driver.title.split("for PC", 1)[0]
    name = name.replace("™","")
    name = name.replace("®","")
    onwindow = "Windows"
    onmac = "Not on Mac"
    developer = driver.find_element_by_xpath("//*[@ng-bind-html='::developerLink.label']").text
    publisher = driver.find_element_by_xpath("//*[@ng-bind-html='::publisherLink.label']").text
    launcher = "Origin"
    Seller = "Origin.com"
    game_release = driver.find_element_by_xpath("//*[@ng-bind-html='formattedReleaseDate']").text
    d = datetime.datetime.strptime(game_release.strip(), '%B %d, %Y')
    game_release = d.strftime('%Y-%m-%d')

    platform = driver.find_element_by_xpath("//*[@class='otkicon otkicon-windows']")
    platform2 = ""
    try:
        platform2 = driver.find_element_by_xpath("//*[@class='otkicon otkicon-apple']")
    except:
        pass

    try:
        current_price = driver.find_element_by_xpath("//*[@class='origin-white-space-nowrap']").text
        if (re.search('[a-zA-Z]', current_price) == False):
            (Error)
    except:
        try:
            driver.find_element_by_xpath("//*[@class='otkbtn otkbtn-primary otkbtn-primary-btn']").click()
            driver.implicitly_wait(5)
            time.sleep(2)
            current_price = driver.find_element_by_xpath("//*[@class='origin-white-space-nowrap']").text
        except:
            print("Nopeplatform")
            driver.quit()
            exit(0)

    
    if platform != "" and platform2 != "":
        MacWin = "Windows, Macintosh"

    if conn is not None:
        create_table(conn, game_table)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        
        savings_price = 0
        current_price = Decimal(current_price[1:])
        current_price = (round(float(current_price),2))
        original_price = current_price
        game = (name, Seller,game_release, original_price, current_price, MacWin, launcher, savings_price, developer, publisher)
        insert_game(conn, game)
    # print(name)
    # print(current_price)
    # print(developer)
    # print(publisher)
    # print(game_release)

    driver.quit()
    print (get_game_info(conn,name))
