from scrapy.item import Item, Field


class StackItem(Item):
    title = Field()
    url = Field()


class OCCItem(Item):
    title = Field()
    url = Field()


class IndeedItem(Item):
    title = Field()
    url = Field()