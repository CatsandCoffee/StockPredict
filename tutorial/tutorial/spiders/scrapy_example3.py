import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'saltworks'

    start_urls = ['https://www.saltworkstech.com/news/']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.elementor_post__title + a::attr(href)'):
            print("""hre
            
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            sdf
            f""")
            yield response.follow(href, self.parse_author)

    #     # follow pagination links
    #     for href in response.css('li.next a::attr(href)'):
    #         yield response.follow(href, self.parse)

    # def parse_author(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).get(default='').strip()

    #     yield {
    #         'name': extract_with_css('h3.elementor-post__badge::text'),
    #         'birthdate': extract_with_css('.text'),
    #         'bio': extract_with_css('.author-description::text'),
    #     }
