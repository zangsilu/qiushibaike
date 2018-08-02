# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiushibaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    avatar = scrapy.Field()
    content = scrapy.Field()
    contentImage = scrapy.Field()
    praiseCount = scrapy.Field()
    commentCount = scrapy.Field()
    comment = scrapy.Field()
    nextPage = scrapy.Field()
    pass
