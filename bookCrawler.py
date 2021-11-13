import scrapy


class bookSpider(scrapy.Spider):
    name = 'bookworm'

    start_urls = [
        'http://books.toscrape.com'
    ]

    def parse(self, response):
        for item in response.css('ol.row li'):
            yield{
                'image_url': item.css('a img ::attr(src)').get(),
                'book_title': item.css('a::text').get(),
                'product_price': item.css('p.price_color::text').get()
            }
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
