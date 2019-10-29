# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class BgmeaItem(Item):
    Name = Field()
    Designation = Field()
    Company_Name = Field()
    EmailID = Field()
    Phone_Number = Field()
    Address = Field()


