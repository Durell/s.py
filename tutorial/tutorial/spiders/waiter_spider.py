import scrapy

class WaiterSpider(scrapy.Spider):
    name = "waiter"

    start_urls = [
        'https://sandiego.craigslist.org/search/fbh?sort=date&query=server',
    ]

    def parse(self, response):
        for line in response.css('p.result-info'):
            title = line.css('a.result-title::text').get();
            date = line.css('time::attr(datetime)').get();
            link = line.css('a.result-title::attr(href)').get();
            if 'server' in title.lower():
                yield scrapy.Request(link, callback=self.parse);
