import scrapy



class Details(scrapy.Item):
    price      = scrapy.Field()
    type       = scrapy.Field()
    price_m2   = scrapy.Field()
    floor      = scrapy.Field()
    furnishing = scrapy.Field()
    market     = scrapy.Field()
    building   = scrapy.Field()
    area       = scrapy.Field()
    rooms      = scrapy.Field()

class OlxScrapyDetailsSpider(scrapy.Spider):
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }
    name = 'olx_scrapy_details'
    allowed_domains = ["www.olx.pl"] 
    try:
        with open("olx_links_scrapy.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        det = Details()

        price_xpath       = '//h3[contains(@class, "css-ddweki er34gjf0")]/text()'
        type_xpath        = '//ul[contains(@class, "sfcl1s")]/li[1]/p/span/text()'
        price_m2_xpath    = '//ul[contains(@class, "css-sfcl1s")]/li[2]/p/text()'
        floor_xpath       = '//ul[contains(@class, "css-sfcl1s")]/li[3]/p/text()'
        furnishing_xpath  = '//ul[contains(@class, "css-sfcl1s")]/li[4]/p/text()'
        market_xpath      = '//ul[contains(@class, "css-sfcl1s")]/li[5]/p/text()'
        building_xpath    = '//ul[contains(@class, "css-sfcl1s")]/li[6]/p/text()'
        area_xpath        = '//ul[contains(@class, "css-sfcl1s")]/li[7]/p/text()'
        rooms_xpath       = '//ul[contains(@class, "css-sfcl1s")]/li[8]/p/text()'
 
        det['price']      = response.xpath(price_xpath).getall() 
        det['type']       = response.xpath(type_xpath).getall()
        det['price_m2']   = response.xpath(price_m2_xpath).getall()
        det['floor']      = response.xpath(floor_xpath).getall()
        det['furnishing'] = response.xpath(furnishing_xpath).getall()
        det['market']     = response.xpath(market_xpath).getall()
        det['building']   = response.xpath(building_xpath).getall()
        det['area']       = response.xpath(area_xpath).getall()
        det['rooms']      = response.xpath(rooms_xpath).getall()

        yield det
