# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class TwitterscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class TwitterBotItem(Item):
    phone = Field()
    company = Field()
    locality = Field()
    region = Field()
    postalcode = Field()
    street_address = Field()