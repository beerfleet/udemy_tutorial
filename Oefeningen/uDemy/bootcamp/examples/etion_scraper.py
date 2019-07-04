# http://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://etion.be/']
    
    def parse(self, response):
        for article in response.css('.row'):
            yield {
                'price': article.css("H2").extract_first(),
                'title': article.css(".col-md-6").extract_first()
            }
            #next = response.css(".next > a::attr(href)").extract_first() # next page ?
            #if next:
            #    yield response.follow(next, self.parse) # recursion -> call parse with next
