from simhash import Simhash
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class RadialSpiderArch(CrawlSpider):
    name = "radialArch"
    temp=[""]
    allowed_domains = [
     'web.archive.org',
    ]
    start_urls = [
     'https://web.archive.org/web/20120901120120/iskme.org',
    ]
    
    custom_settings = {
        'DEPTH_LIMIT': '5'
    }
    rules = (Rule(LinkExtractor(allow='\/web\/2012[0-9]{10}\/http:\/\/iskme\.org\/([a-zA-Z]+)'),callback='parse_item', follow=True),)
    def parse_item(self, response):
        page= response.xpath('//html/*')
        yield {
                'Simhash': Simhash(page.extract()).value,
                'url': response.url,
                'depth' : response.meta['depth'],
                'referer': str(response.request.headers['Referer'])
                }