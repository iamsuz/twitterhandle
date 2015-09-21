__author__ = 'Sujit'

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import TakeFirst, Join, MapCompose
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.item import Item
from urlparse import urljoin
import re
import sys
import re
import json
from scrapy.spider import BaseSpider

from twitterscrapy.items import TwitterBotItem

class TwitterBotCrawlSpider(CrawlSpider):

    name = 'twitterbotSpider'

    def __init__(self, *args, **kwargs):
        global rules
        # query = query.replace(' ','-')
        # city = city.replace(' ','-')
        self.rules = (Rule(SgmlLinkExtractor(allow=('/'+'*')), callback='parse_item',follow = True),)
        super(TwitterBotCrawlSpider, self).__init__(*args, **kwargs)
        self.allowed_domains = ['www.twitter.com']
        self.start_urls = [kwargs.get('start_url')]
        print(self.start_urls)

    def parse_item(self,response):

        l = XPathItemLoader(item=TwitterBotItem(),response=response)
        print "###################"
        l.add_xpath('company','//*[@class="trends-inner"]/div/div[2]/ul/li[1]/a/text()')
        l.add_xpath('street_address','//*[@id="info-container"]/div[1]/dl/dd[1]/span[1]/text()')
        l.add_xpath('locality','//*[@id="info-container"]/div[1]/dl/dd[1]/span[2]/text()')
        l.add_xpath('region','//*[@id="info-container"]/div[1]/dl/dd[1]/span[3]/text()')
        l.add_xpath('postalcode','//*[@id="info-container"]/div[1]/dl/dd[1]/span[4]/text()')


        res = l.load_item()

        results = {'name':'','address':''}

        if 'company' in res:
            results['name'] = res['company']
        if 'street_address' in res:
            results['address'] = res['street_address']
        if 'locality' in res:
            results['address'] = results['address'] + res['locality']
        if 'region' in res:
            results['address'] = results['address'] + res['region']
        if 'postalcode' in res:
            results['address'] = results['address'] + res['postalcode']

        return res


