import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from app.item import PageItem

class WebSiteSpider(CrawlSpider):
    name            = 'website_spider'

    rules = (
        Rule(LinkExtractor(), callback='parse_item'),
    )

    def __init__(self, start_url, domain, **kwargs):
        self.allowed_domains = [domain]
        self.start_urls      = [start_url]
        super().__init__(**kwargs)

    def parse_item(self, response):
        self.logger.info(response.url)
        item = PageItem()
        item['url'] = response.url
        return item
