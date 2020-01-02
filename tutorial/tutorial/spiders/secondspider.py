import scrapy

class SecondSpider(scrapy.Spider):
    name = "SecondSpider"
    start_urls = [
        "https://saltworkstech.com/news/"
    ]
    
    def parse(self, response):
        links = response.xpath()
