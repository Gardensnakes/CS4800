from django.http import HttpResponse
import sqlite3
from sqlite3 import Error
import decimal 

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

sql_path = r"C:\\Users\\Administrator\\Desktop\\testsite\\helloworld\\Games.db"
conn = sqlite3.connect(sql_path, check_same_thread=False)
def get_game_info(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM game_info WHERE Name=?", (game_name,))
    rows = cur.fetchall()
    game_items = []
    for row in rows:
        game_items.append(row)
    return game_items

def decode_name(urlname):
    return urlname.replace("+"," ")

def get_game_name(conn, encrip_name):
    decoded_name =decode_name(encrip_name)
    cur = conn.cursor()
    cur.execute("SELECT Name FROM game_info WHERE Name=?", (decoded_name,))
    game_items = []
    for row in cur:
        name = row[0]
    return name

def get_game_1seller(conn, game_name):
    try:
        conn = create_connection(sql_path)
        cur = conn.cursor()
        game_items = []
        i = 0
        num_of_rows = cur.execute("SELECT DISTINCT seller FROM game_info WHERE Name=?", (game_name,))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            game_items.append(row[0])
                # 
        return game_items[0]   
    except: 
        return ""


def get_game_2seller(conn, game_name):
    try:
        conn = create_connection(sql_path)
        cur = conn.cursor()
        game_items = []
        i = 0
        num_of_rows = cur.execute("SELECT DISTINCT Seller FROM game_info WHERE Name=?" , (game_name,))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            game_items.append(row[0])
                # 
        return game_items[1]   
    except: 
        return ""

def get_game_3seller(conn, game_name):
    try:
        conn = create_connection(sql_path)
        cur = conn.cursor()
        game_items = []
        i = 0
        num_of_rows = cur.execute("SELECT DISTINCT Seller FROM game_info WHERE Name=?", (game_name,))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            game_items.append(row[0])
                # 
        return game_items[2]   
    except: 
        return ""
#


def get_game_4seller(conn, game_name):
    try:
        conn = create_connection(sql_path)
        cur = conn.cursor()
        game_items = []
        i = 0
        num_of_rows = cur.execute("SELECT DISTINCT Seller FROM game_info WHERE Name=?", (game_name,game_name))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            game_items.append(row[0])
                # 
        return game_items[3]   
    except: 
        return ""


def get_game_5seller(conn, game_name):
    gamename_space = game_name + " "
    try:
        conn = create_connection(sql_path)
        cur = conn.cursor()
        game_items = []
        i = 0
        num_of_rows = cur.execute("SELECT DISTINCT Seller FROM game_info WHERE Name=? OR Name = ?",(game_name,gamename_space))
        while True:
            row = cur.fetchone()
            if row == None:
                break
            game_items.append(row[0])
                # 
        return game_items[4]   
    except: 
        return ""

def commission_cost(price,seller):
    if seller == "Steam.com":
        return "$" + str(round(price * .30),2) + " Commission"
    elif seller == "Humblebundle.com":
        return "$" + str(round(price * .15),2) + " default commission"
    elif seller == "GOG.com":
        return "$" + str(round(price * .30),2) + " Commission"
    elif seller == "Origin.com":
        return "$" + str(price + "Commission Uknown")
    elif seller == "EpicGames.com": 
        return "$" + str(round(price * .12),2) + " Commission"
    else:
        return price

def get_game_release(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT game_release FROM game_info WHERE Name=? AND game_release IS NOT NULL LIMIT 1" , (game_name,))
    game_release = ""   
    for row in cur:
        game_release = game_release + str(row)
    return game_release[2:-3]


def get_game_original_price(conn, game_name,seller):
    cur = conn.cursor()
    cur.execute("SELECT original_price FROM game_info WHERE Name=? AND Seller = ? ORDER BY date_scraped ASC", (game_name,seller))
    price = ""
    for row in cur:
        price = row[0]
        price = str(price)
    if price != "":
        return price
    else:
        return ""
    
def get_game_current_price(conn, game_name,seller):
    cur = conn.cursor()
    cur.execute("SELECT current_price FROM game_info WHERE Name=? AND Seller =? ORDER BY date_scraped ASC", (game_name,seller))
    price = ""
    for row in cur:
        price = row[0]
        #price = str(price)
    if price != "":
        if seller == "Steam.com":
            commission = str(round((price * .30),2))
            commission = " ($" + commission + " commission)"
            price = str(price)
            return "$" + price  + commission
        elif seller == "Humblebundle.com":
            commission = str(round((price * .15),2))
            commission = " ($" + commission + " commission)"
            price = str(price)
            return "$" + price  + commission
        elif seller == "GOG.com":
            commission = str(round((price * .3),2))
            commission = " ($" + commission + " commission)"
            price = str(price)
            return "$" + price  + commission
        elif seller == "Origin.com":
            price = str(price)
            return "$" + price + " (commission uknown)"
        elif seller == "EpicGames.com": 
            commission = str(round((price * .12),2))
            commission = " ($" + commission + " commission)"
            price = str(price)
            return "$" + price  + commission
        else:
            return ""
    else:
        return ""

def get_game_lowest(conn, game_name,seller):
    cur = conn.cursor()
    cur.execute("SELECT current_price FROM game_info WHERE Name =? AND Seller =? ORDER BY current_price ASC LIMIT 1", (game_name,seller))
    game_items = []
    price = ""
    for row in cur:
        price = row[0]
        price = str(price)
    if price != "":

        return ("$" + price)
    else:
        return ""

def get_desc(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT description FROM game_info WHERE Name =? AND description != 'No game description at this time'", (game_name,))
    desc="No game description at this time"
    for row in cur:
        desc = (row[0])
    return desc

print(get_desc(conn,'Hades'))
def get_abs_lowest(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT current_price FROM game_info WHERE Name =? AND Seller =? ORDER BY current_price ASC LIMIT 1", (game_name,seller))
    price = ""
    for row in cur:
        price = row[0]
        price = str(price)
    if price != "":
        return ("$" + price)
    else:
        return ""

def get_lowest_price(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT current_price, date_scraped  FROM game_info WHERE Name =? ORDER BY date_scraped DESC, current_price ASC LIMIT 1", (game_name,))
    price = ""
    for row in cur:
        price = row[0]
        price = str(price)
    if price != "":

        return ("$" + price)
    else:
        return ""


def get_lowest_seller(conn, game_name):
    seller =""
    cur = conn.cursor()
    cur.execute("SELECT seller FROM game_info WHERE Name =? ORDER BY date_scraped DESC, current_price ASC LIMIT 1", (game_name,))
    for row in cur:
        seller = row[0]
    return seller

#def get_lowest(conn, game_name,launcher):
#     cur = conn.cursor()
#     cur.execute("SELECT current_price FROM game_info WHERE Name =? AND launcher =? ORDER BY current_price ASC LIMIT 1", (game_name,launcher))
#     game_items = []
#     price = ""
#     for row in cur:
#         price = row[0]
#         price = str(price)
#     if price != "":

#         return ("$" + price)
#     else:
#         return ""

def get_game_platform(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT MacWin FROM game_info WHERE Name=? AND MacWin IS NOT NULL", (game_name,))
    platform = ""
    for row in cur:
        platform = row[0]
    return platform

def get_game_launcher(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT launcher FROM game_info WHERE Name=? AND launcher IS NOT NULL", (game_name,))
    i = 0
    launcher = ""
    for i in cur:
        launcher = launcher + ',' + (i[0])

    return launcher[1:]

def get_game_savings(conn, game_name,seller):
    cur = conn.cursor()
    cur.execute("SELECT savings_price FROM game_info WHERE Name=? AND savings_price IS NOT NULL", (game_name,))
    seller = ""
    for row in cur:
        seller = row[0]
    return seller

def get_game_developer(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT developer FROM game_info WHERE Name=? AND developer IS NOT NULL", (game_name,))
    i = 0
    dev = ""
    for i in cur:
        dev = dev + ',' + (i[0])
    return dev[1:]

def get_game_publisher(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT publisher FROM game_info WHERE Name=? AND publisher IS NOT NULL", (game_name,))
    i = 0
    pub = ""
    for i in cur:
        pub = pub + ',' + (i[0])
    return pub[1:]

def return_prediction(conn, game_name):
    cur = conn.cursor()
    cur.execute("SELECT avg(current_price) FROM game_info WHERE Name =?", (game_name,))
    game_items = []
    for row in cur:
        avg = row[0]
    cur.execute("SELECT current_price FROM game_info WHERE Name =? ORDER BY date_scraped DESC LIMIT 1", (game_name,))
    game_items = []
    if cur != None:
        for row in cur:
            current_price = row[0]
            math = str(round(current_price - avg,2))  
        if (avg  < current_price):
            math_percent= 100 - ((avg/current_price) * 100)
            return ("We do not recommend buying at this time, as the current price is UP by $"+ math +" or %" + str(round(math_percent,2)))
            
        elif (avg == current_price):
            return("The current price is equal to the average price at $" + str(current_price)) + ", so no recommondations"
        elif  (avg > current_price):
            math_percent= ((current_price/avg) * 100) - 100
            return "The current price is DOWN by $" + math[1:] + " or %"+ str(round(math_percent,2))[1:] + " Today! We recommend buying now!"
        else:  
            return"No assessment"









# sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
# conn = create_connection(sql_path)
# print(get_game_seller(conn,'Hades'))


#print (get_game_info(conn,'Hades'))
# def main():
#     sql_path = r"C:\\Users\\TJ\\Desktop\\ProjectSite\\helloworld\\Games.db"
#     conn = create_connection(sql_path)
#     game_name = "Hades"
#     with conn:
#         game_info = get_game_info(conn, game_name)
#     for entry in game_info:
#        # return HttpResponse(entry)
#        print(entry)


#main()