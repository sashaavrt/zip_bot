# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor


# class TestSpider(CrawlSpider):
#     name = "test"
#     allowed_domains = ["ru.wikipedia.org"]
#     start_urls = ["https://ru.wikipedia.org/wiki/%D0%9D%D0%90%D0%A1%D0%90"]
#     rules = (Rule(LinkExtractor(allow=(''))))
   

import scrapy
import re
import urllib.parse
from urllib.parse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from scrapy.item import Item, Field
from scrapy.pipelines.images import ImagesPipeline
from firstP.items import Site
from firstP.items import ImageItem

class firstPSpider(scrapy.Spider):
    name = "firstP"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = ["https://ru.wikipedia.org/wiki/%D0%9D%D0%90%D0%A1%D0%90"]

def parse(self, response):
    for sel in response.xpath('//html/body'):
        item = Site()
        img_url = sel.xpath('//a[@idd="followclaslink"]/@href').extract()[0]
        yield scrapy.Request(urlparse.urljoin(response.url, img_url),callback=self.parseImages,  meta={'item': item})

def parseImages(self, response):
    for elem in response.xpath("//img"):
        img_url = elem.xpath("@src").extract_first()
        yield ImageItem(image_urls=[img_url])