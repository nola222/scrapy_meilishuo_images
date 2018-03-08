# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MeilishuoPipeline(object):
    def process_item(self, item, spider):
        print(item['image_urls'])
        return item

