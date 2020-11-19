from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait     
import time 

PATH = "C:\\Users\\TJ\\Desktop\\testsite\\helloworld\\geckodriver.exe"

def google_Humble(title):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
      
    # to search 
    query = title +" Humblebundle.com"
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        first_link = j

    driver = webdriver.Firefox(executable_path=PATH)
    driver.get(first_link)
    driver.maximize_window() #For maximizing window
    driver.implicitly_wait(10) #gives an implicit wait for 10 seconds
    name = driver.title.split(" from the Humble Store", 1)[0]
    name = name.replace('Buy ','')
    price = driver.find_element_by_class_name('current-price').text

    #driver.find_element_by_xpath("//*[@class='otkbtn otkbtn-primary otkbtn-primary-btn']")

    #print (driver.find_element_by_css_selector('.js-property-value property-value a').get_attribute('href'))


    #print(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-entity-kind='display_item']/a"))).get_attribute('href'))
    
    print(price)

    driver.quit()
google_Humble('CoD Cold War')