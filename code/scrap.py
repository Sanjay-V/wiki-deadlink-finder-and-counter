from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

class LinkItem(Item):
    url = Field()
    Link = Field()
    status = Field()

class LinkSpider(CrawlSpider):
    name = "linkSpider"

    # Filter out other sites. No need dig into outside websites and check their links.
    allowed_domains = ["en.wikipedia.org"]

    # String together multiple domains if needed with a comma (,)
    # i.e. ['https://www.matthewhoelter.com', 'https://blog.matthewhoelter.com']
    start_urls = ["https://en.wikipedia.org/wiki/Wiki"] 

    handle_httpstatus_list = [404]
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)

    def parse_item(self, response):
        if response.status == 404:
            link = LinkItem()

            link['url'] = response.url
            link['status'] = response.status
            link['Link'] = response.request.headers.get('Referer')

            return link