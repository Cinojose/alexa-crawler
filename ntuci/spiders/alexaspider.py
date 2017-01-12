# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import sys

class AlexaspiderSpider(CrawlSpider):
    name = "alexaspider"
    allowed_domains = ["alexa.com"]
    start_urls = (
       'http://www.alexa.com/topsites/category/Top/News',
    )
    rules = (
        Rule(SgmlLinkExtractor(allow=(), restrict_xpaths=('//ul[contains(@class, "subcategories span3")]',)), callback="parse_page", follow= True),
    )
    def parse_page(self, response):
      print response
      for sel in response.xpath('//li[contains(@class,"site-listing")]'):
        names = sel.xpath('//p[contains(@class,"desc-paragraph")]/a/text()').extract()
	f = open("/home/ubuntu/scrapy/url.txt","a")
	for url in names:
		print url
		f.write(url)
		f.write("\n")
	f.close()
 #       sys.exit()
