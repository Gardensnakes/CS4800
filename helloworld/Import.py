# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

PATH = "C:\\Users\\TJ\\OneDrive\\Documents\\GitHub\\CS4800\\helloworld\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://www.epicgames.com/store/en-US/product/watch-dogs-legion/home')
print(driver.title)

price = driver.find_element_by_xpath("//*[@data-component='Price']")
print(price.text)
driver.quit()