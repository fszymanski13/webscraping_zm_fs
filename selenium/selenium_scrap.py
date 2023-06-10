from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass
import datetime
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
# reading the necessary webdriver
gecko_path = 'chromedriver_win32\chromedriver'
ser = Service(gecko_path)
options = webdriver.chrome.options.Options()
options.headless = False
driver = webdriver.Chrome(options = options, service=ser)

start_time = time.time()
# Set the boolean parameter to limit the number of pages
limit_links = True  

#creating the list of links to scrape the ads from


urls = ["https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/"] + [f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page={page}" for page in range(2, 25)]

#initiation of the empty links list
links = []

#going through the elements of the list and adding the links to the ads to the previously created empty list

for url in urls:
    driver.get(url)
    if url==urls[0]:
        #accepting the cookies on the first page
        button = driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
        button.click()

    time.sleep(10)
    #finding all the links 
    links_page = driver.find_elements(By.XPATH, '//a[@class="css-rc5s2u"]')
    for link in links_page:
        #appending links one by one to the list
        links.append(link.get_attribute('href'))
    time.sleep(5)

links = [link for link in links if link.contains('olx.pl')]
if limit_links: 
    links = links[0:101]
#creating a dataframe and exporting to csv
links_df = pd.DataFrame({'link': links})
links_df.to_csv('links_selenium.csv', index= False)

end_time = time.time()
execution_time = end_time - start_time

print(execution_time)


