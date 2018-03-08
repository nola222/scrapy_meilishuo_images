1.使用scrapy框架默认ImagesPipeline管道抓取美丽说5页图片

2. settings.py中启用ImagesPipeline写法：
	ITEM_PIPELINES = {
		# 'MeiLiShuo.pipelines.MeilishuoPipeline': 300,
		# 固定写法 权重自定义
		'scrapy.contrib.pipeline.images.ImagesPipeline':200
	}

3. settings.py中图片设置信息 固定写法
	# 图片存储配置
	# 图片存放位置
	IMAGES_STORE = './images'

	# 缩略图 大小自定义
	# IMAGES_THUMBS = {
	#     'small': (50, 50),
	#     'big': (270, 270),
	# }

4. items.py字段固定写法
	class MeilishuoItem(scrapy.Item):
	    # define the fields for your item here like:
	    # name = scrapy.Field()
		# 使用默认的图片管道 ImagesPipeline  定义的字段固定写法  需要在settings开启管道

		# image_urls 抓取项目的urls放在这
	    image_urls = scrapy.Field()
	    images = scrapy.Field()