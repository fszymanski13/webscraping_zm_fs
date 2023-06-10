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
import numpy as np


#reading the file with links to scrape the information from

links_df = pd.read_csv('links_selenium.csv')

#webdriver
gecko_path = 'chromedriver_win32\chromedriver'
ser = Service(gecko_path)
options = webdriver.chrome.options.Options()
options.headless = False
driver = webdriver.Chrome(options = options, service=ser)

#initiation of an empty dataframe
scraped_data = pd.DataFrame({'Type': [], 'Price':[], 'Price per m2': [], 'Floor': [], 'Furnishing':[],
                   'Market':[], 'Type of building':[], 'Area':[], 'Number of rooms':[]})

start_time = time.time()

#reading and saving the information about type, price, price per m2, floor, furnishing, market, surface, building type, number of rooms

for url in links_df['link']:
    driver.get(url)
    if url==links_df['link'][0]:
        #accepting cookies
        button = driver.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
        button.click()
        time.sleep(10)
    try:
        price = driver.find_element(By.XPATH, '//div[@data-testid="ad-price-container"]').get_attribute('textContent')
    except:
        price = np.nan

    try:
        price_m = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[2]/p').get_attribute('textContent')
    except:
        price_m = np.nan 
    try:
        type = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[1]/p/span').get_attribute('textContent')
    except:
        type = np.nan
    try:
        floor = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[3]/p').get_attribute('textContent')
    except:
        floor = np.nan
    try:
        furnishing = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[4]/p').get_attribute('textContent')
    except:
        furnishing = np.nan

    try:
        mkt = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[5]/p').get_attribute('textContent')
    except:
        mkt = np.nan

    try:
        btype = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[6]/p').get_attribute('textContent')
    except:
        btype = np.nan

    try:
        area = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[7]/p').get_attribute('textContent')
    except:
        area = np.nan
    try:
        no_rooms = driver.find_element(By.XPATH, '//ul[@class="css-sfcl1s"]/li[8]/p').get_attribute('textContent')
    except:
        no_rooms = np.nan

    house_data = {'Type':type, 'Price': price, 'Price per m2': price_m, 'Floor': floor, 'Furnishing': furnishing,
                   'Market': mkt, 'Type of building': btype, 'Area': area, 'Number of rooms': no_rooms }

    scraped_data = scraped_data.append(house_data, ignore_index=True)
    time.sleep(5)

end_time = time.time()
execution_time = end_time - start_time
time_execution = pd.DataFrame({"time": [execution_time]})

#exporting dataframe to csv
scraped_data.to_csv('selenium_df_scraped_2.csv')
print(time_execution)
print(scraped_data)
