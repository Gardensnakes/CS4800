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
                                        );"""
if conn is not None:
        create_table(conn, game_table)                                        
def google_steam(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" steam store"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    if (first_link.find("steampowered") != -1):
        html = urlopen(first_link)
        bs = BeautifulSoup(html, 'html.parser')
    
    # Find game name and prints it
    game_name = bs.find("div", {"class":"apphub_AppName"})
    game_name = game_name.get_text()
    #print(game_name)
    game_name = game_name.replace("™","")
    game_name = game_name.replace("®","")
    Seller = "Steam.com"

    launcher = "Steam"
    for a in bs.find_all("div",{"class":"DRM_notice"}):
        this = (a.get_text().strip())
        treasure = (this.find("Origin"))
        if (treasure != -1):
            launcher = "Origin"

    game_platform = bs.find("span",{"class":"platform_img win"})
    game_platform2 = bs.find("span",{"class":"platform_img mac"})
    release_date = bs.find("div",{"class":"date"}).get_text()
    #print(release_date)
    game_details = bs.find("div",{"class":"glance_ctn_responsive_left"})
    count = 0;
    # for a in bs.find_all("div",{"class":"dev_row"}):
    #   if count == 0:
    #       print (a.get_text())
    #       coutn = count + 1
    #   if count == 1:
    #       print (a.get_text())
    #       count = count + 1
    for a in game_details.find_all('a', href=True):
        if count == 0:
            game_dev = a.get_text()
            # print ("Dev: ", game_dev)
        if (count == 1) and (a.get_text().find("(Mac)") != -1):
            game_dev = game_dev+ ", " + a.get_text()
        else:
            publisher = a.get_text()
        if (count == 2):
            publisher = a.get_text()
        if count == 3:
            publisher = publisher+ ", " + a.get_text()
        count= count + 1

    d = datetime.datetime.strptime(release_date.strip(), '%b %d, %Y')
    release_date = d.strftime('%Y-%m-%d')
    #print(d.strftime('%Y-%m-%d'))


    if game_platform is not None:
        # print("Supported on: Windows")
        MacWin = "Windows"

    if game_platform2 is not None:
        # print("Supported on: Mac")
        MacWin = MacWin + ", Macintosh"

    # Looks in first section of steam section "add to cart"
    main = bs.find("div",{"class":"game_area_purchase_game"})
    sub_area = main.find("div",{"class":"game_purchase_price price"})

    # If it can't find a non-on-sale game price in the first section, check the next section
    if (sub_area is None):
        main = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['game_area_purchase_game_wrapper']))
        sub_area = main.find("div",{"class":"game_purchase_price price"})

    # if game is not on sale
        if sub_area is not None:
            final = (sub_area.get_text())
            #print (final.strip())
            final = Decimal(final.strip()[1:])
            final = (round(float(final),2))
            original_price = final
            savings = 0
            game = (game_name,Seller, release_date, original_price, final, MacWin, launcher, savings, game_dev, publisher)
            insert_game(conn, game)

        else:
            sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
            sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
            final = sub_area.get_text()
            original = sub_area2.get_text()
            # print("The Final Price is " + final.strip())
            # print("The Original Price is " + original.strip())
            # print("You save " )
            final = Decimal(final.strip()[1:])
            final = (round(float(final),2))
            original = Decimal(original.strip()[1:])
            original = (round(float(original),2))
            savings = round(original - final)
            # print("You save ", savings)

            game = (game_name,Seller, release_date, original, final, MacWin, launcher, savings, game_dev, publisher)
            insert_game(conn, game)

    # Game must not be on sale
    elif (sub_area is not None):
        final = (sub_area.get_text())
        #print (final.strip())
        final = Decimal(final.strip()[1:])
        final = (round(float(final),2))
        original = final
        savings = 0
        game = (game_name,Seller, release_date, original, final, MacWin, launcher, savings, game_dev, publisher)
        insert_game(conn, game)


    else:
        try:
            sub_area = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_final_price']))
            sub_area2 = bs.find((lambda tag: tag.name == 'div' and tag.get('class') == ['discount_original_price']))
            final = sub_area.get_text()
            original = sub_area2.get_text()
            # print("The Final  Price is " +final.strip())
            # print("The Original Price is " + original.strip())
            

            final = Decimal(final.strip()[1:])
            final = (round(float(final),2))
            original = Decimal(original.strip()[1:])
            original = (round(float(original),2))
            savings = round(original - final)
            # print("You save ", savings)

            game = (game_name,Seller, release_date, original, final, MacWin, launcher, savings, game_dev, publisher)
            insert_game(conn, game)

        except:
            exit(0)
    print (get_game_info(conn,game_name))


