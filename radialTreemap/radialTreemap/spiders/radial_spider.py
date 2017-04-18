from simhash import Simhash
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class RadialSpider(CrawlSpider):
    name = "radial"
    temp=[""]
    allowed_domains = [
     'aetos.it.teithe.gr',
    ]
    start_urls = [
     'http://aetos.it.teithe.gr/~adamidis/',
    ]

    rules = (Rule(LinkExtractor(allow=allowed_domains), callback='parse_item', follow=True),)
    
    def parse_item(self, response):
        quote= response.xpath('//html/*') 
        yield {
            'Simhash': Simhash(quote.extract()).value,
            'url': response.url,
            'depth' : response.meta['depth']
        }
