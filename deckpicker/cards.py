import scrapy

class DeckpickerCard(scrapy.Item):
    title = scrapy.Field()
    count = scrapy.Field()
    price = scrapy.Field()
