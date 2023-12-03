# OLX House Data Scraping Project

This project is designed to scrape house data from the OLX website. It demonstrates the use of three different web scraping techniques using Python: BeautifulSoup, Scrapy, and Selenium. 

## Description

The project contains three main components, each utilizing a different library or framework for web scraping:

- **BeautifulSoup**: Used for parsing HTML and extracting the data needed.
- **Scrapy**: An open-source web crawling framework, used to scrape large amounts of data efficiently.
- **Selenium**: A tool for automating web browsers, used here to simulate user interaction and scrape dynamic content.

## Libraries Used

- BeautifulSoup (`bs4`)
- Scrapy
- Selenium
- pandas
- urllib
- re (Regular Expressions)
- os
- datetime
- getpass
- time

## How to run olx_scraper_beautiful_soup
1. set your cd to the soup folder
2. run the code


## How to run olx_scrapy

1. open cmd
2. \>cd 'directory of the scraper' (the file where the scrapy.cfg is located) (in my case it is C:\Studia\Master\WebScraping\Project\olx_scrapy)
3. \>scrapy startproject olx_scrapy
4. \>cd olx_scrapy
5. Copy files olx_scrapy_links.py and olx_scrapy_details.py to the folder 'spiders'
5. \>scrapy crawl olx_scrapy_links -O olx_links_scrapy.csv
6. \>scrapy crawl olx_scrapy_details -O olx_details_scrapy.csv


## How to run selenium_scrap and selenium_df
1. set your cd to the selenium folder
2. change the path to your webdriver
3. run the code 
