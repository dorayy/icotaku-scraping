import scrapy


class PlanningSpider(scrapy.Spider):
    name = 'planning'
    allowed_domains = ['anime.icotaku.com']
    start_urls = ['http://anime.icotaku.com/']

    def parse(self, response):
        pass
