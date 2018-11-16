from scrapy import Spider

from deckpicker.items import DeckpickerCard

class CardsSpider(Spider):
    name = "cards"
    allowed_comains = ["mtggoldfish.com"]
    start_urls = ["https://www.mtggoldfish.com/archetype/standard-boros-weenie-61393#paper"]

    def parse(self, response):
        cards = response.xpath('//table[@class="deck-view-deck-table\"]/tr[not(contains(td/@class, "deck-header"))]')

        for card in cards:
            item = DeckpickerCard()
            item['title'] = card.xpath('td[2]/a/text()').extract()[0]
            item['count'] = card.xpath('td[1]/text()').extract()[0].strip()
            item['price'] = card.xpath('td[4]/text()').extract()[0].strip()
            yield item
