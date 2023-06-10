import scrapy

limit_links = True

class Link(scrapy.Item):
    link = scrapy.Field()

class OlxScrapyPySpider(scrapy.Spider):
    # Set a custom user agent for the spider
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    # Set the name of the spider
    name = "olx_scrapy_links"

    # Specify the allowed domains for the spider
    allowed_domains = ["www.olx.pl"]

    # Generate and define the URLs for the spider
    start_urls = ["https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/"] + [f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/?page={page}" for page in range(2, 24)]

    # Handle specific HTTP status code
    handle_httpstatus_list = [403]

    # Create a list to store the extracted links
    extracted_links = []

    def start_requests(self):
        # Send a scrapy.Request for each start URL and specify the parse method as the callback
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Define the XPath to extract the links
        xpath = "//a[contains(@class, 'css-rc5s2u')]"
        
        # Extract the links using the XPath 
        links = response.xpath(xpath)
        
        # Extract only links that are not from external site (i.e 'www.otodom.pl' -> these links start with 'https:' as the entire link is included)
        # Concatenate the desired links with 'https://www.olx.pl/' to create list of full links
        extracted_links = ['https://www.olx.pl/' + link.attrib["href"] for link in links if not link.attrib["href"].startswith('https:')]
        
        # Add the extracted links to the list
        self.extracted_links.extend(extracted_links)

        # Create a Link item for each extracted link and yield it
        if limit_links:    
            for link in extracted_links:
                l = Link()
                l['link'] = link
                yield l
                # break if limit_links is True
                if len(self.extracted_links) >= 100:
                    break
        else:
            for link in extracted_links:
                l = Link()
                l['link'] = link
                yield l

