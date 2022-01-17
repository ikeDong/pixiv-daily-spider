# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class PScrapyItem(scrapy.Item):
    img_name = Field()
    img_author = Field()
    img_id = Field()
    img_page = Field()
    img_rank = Field()
    
    
    