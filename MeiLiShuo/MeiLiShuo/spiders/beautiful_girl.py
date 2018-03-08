# -*- coding: utf-8 -*-
import scrapy
from ..items import MeilishuoItem
from scrapy.http import Request


class BeautifulGirlSpider(scrapy.Spider):
	name = 'beautiful_girl'
	allowed_domains = ['www.meilishuo.com']
	# start_urls = ['http://www.meilishuo.com/search/catalog/10057050?&page=1&action=skirt']

	# 请求5页裙子图片  重写下面这个方法
	def start_requests(self):
		base_url = 'http://www.meilishuo.com/search/catalog/10057050?&page={0}&action=skirt'
		for i in range(1,6):
			url = base_url.format(i)

			yield Request(url=url,callback=self.parse)

	def parse(self, response):
		# 实例化items
		item = MeilishuoItem()
		img_urls = response.xpath('//div[@class="img-size data-ptp-item"]/a')
		for img_url in img_urls:
			image_url = img_url.xpath('./@data-src').extract_first()
			item['image_urls'] = [image_url]

			yield item

