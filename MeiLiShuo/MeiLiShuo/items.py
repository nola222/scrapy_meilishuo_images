# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeilishuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	# 使用默认的图片管道 ImagesPipeline  定义的字段固定写法  需要在settings开启管道

	# image_urls 抓取项目的urls放在这
    image_urls = scrapy.Field()
    images = scrapy.Field()
