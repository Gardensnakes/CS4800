from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time 

PATH = "C:\\Users\\TJ\\Desktop\\testsite\\helloworld\\geckodriver.exe"

# COUNT = 0
def google_gog(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" gog.com"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    html = urlopen(first_link)
    bs = BeautifulSoup(html, 'html.parser')    

    driver = webdriver.Firefox(executable_path=PATH)
    driver.get(first_link)
    time.sleep(4)
    game_details = driver.find_element_by_xpath("//*[@class='product-actions-price__final-amount _price ng-binding']").text
    print(game_details)
    
    driver.quit()
google_gog('Observer Redux')