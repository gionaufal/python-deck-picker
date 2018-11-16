# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeckpickerItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

class DeckpickerCard(scrapy.Item):
    title = scrapy.Field()
    count = scrapy.Field()
    price = scrapy.Field()
