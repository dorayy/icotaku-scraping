# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IcotakuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#À ajouter au fichier items.py
class PlanningItem(scrapy.Item):
    title = scrapy.Field()
    origin = scrapy.Field()
    distribution = scrapy.Field()
    editor = scrapy.Field()
    release = scrapy.Field()
    category = scrapy.Field()
    season = scrapy.Field()
    link = scrapy.Field()

#À ajouter au fichier items.py
class PlanningDetailItem(scrapy.Item):
    titleFr = scrapy.Field()
    titleJp = scrapy.Field()
    origin = scrapy.Field()
    genre = scrapy.Field()
    public = scrapy.Field()
    nbEpisode = scrapy.Field()
    durationEpisode = scrapy.Field()
    editor = scrapy.Field()
    officialWebsite = scrapy.Field()
    story = scrapy.Field()
    img = scrapy.Field()