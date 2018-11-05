from scrapy import Spider

from deckpicker.items import DeckpickerItem

class DeckSpider(Spider):
    name = "deck"
    allowed_domains = ["mtggoldfish.com"]
    start_urls = ["https://www.mtggoldfish.com/metagame/standard/full#paper"]


    def parse(self, response):
        decks = response.xpath('//div[2]/div/h2/span[2]')

        for deck in decks:
            item = DeckpickerItem()
            item['title'] = deck.xpath('a/text()').extract()[0]
            item['url'] = deck.xpath('a/@href').extract()[0]
            yield item
