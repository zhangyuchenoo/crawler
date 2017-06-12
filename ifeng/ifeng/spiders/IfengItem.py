from scrapy.item import Item,Field

class IfengItem(Item):
    title = Field()
    url = Field()
