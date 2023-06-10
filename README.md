How to run olx_scrapy

1. open cmd
2. \>cd 'directory of the scraper' (the file where the scrapy.cfg is located) (in my case it is C:\Studia\Master\WebScraping\Project\olx_scrapy)
3. \>scrapy startproject olx_scrapy
4. \>cd olx_scrapy
5. Copy files olx_scrapy_links.py and olx_scrapy_details.py to the folder 'spiders'
5. \>scrapy crawl olx_scrapy_links -O olx_links_scrapy.csv
6. \>scrapy crawl olx_scrapy_details -O olx_details_scrapy.csv

voilà
