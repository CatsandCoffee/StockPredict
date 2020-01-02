import scrapy

class FirstSpider(scrapy.Spider):
    name = "FirstSpider"

    def start_requests(self):
        urls = [
            # 'https://summitnanotech.ca',
            'https://www.saltworkstech.com/news/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response) :
        for quote in response.css('article') :
            print("Here comes the quote",quote)
            yield {
                'Newslink/Title': quote.css("h3.elementor-post__title").getall()
            }

        # page = response.url.split("/")[-2]1
        # filename = 'quotes123-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

