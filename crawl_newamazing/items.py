# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlNewamazingItem(scrapy.Item):
    pageid = scrapy.Field()
    titleid = scrapy.Field()
    titleurl = scrapy.Field()
    title = scrapy.Field()
    days = scrapy.Field() # 天
    departure_date = scrapy.Field() # 出發日期
    price = scrapy.Field() # price
    total = scrapy.Field()  # 機位
    now = scrapy.Field() # 可售
