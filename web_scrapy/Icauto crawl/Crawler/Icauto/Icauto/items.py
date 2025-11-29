# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IcautoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    car_name = scrapy.Field()
    car_img = scrapy.Field()
    price_field = scrapy.Field()
    model = scrapy.Field()
    city_name = scrapy.Field()
    year1 = scrapy.Field()
    year2 = scrapy.Field()
    year3 = scrapy.Field()
    year4 = scrapy.Field()
    year5 = scrapy.Field()
    image_paths = scrapy.Field()


