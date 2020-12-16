import datetime
import json
import sys
from time import sleep

import scrapy

from scrapysina.items import ScrapyItem


class HuanqiuSpider(scrapy.Spider):
    name = 'huanqiu'
    allowed_domains = ['mil.huanqiu.com/world']
    start_urls = ['https://mil.huanqiu.com/api/list2?node=/e3pmh1dm8/e3pmt7hva&offset=0&limit=20']
    custom_settings = {
        'ITEM_PIPELINES':{
            'scrapysina.pipelines.ScrapyhuanqiuPipeline': 300
        }
    }

    def start_requests(self):
        start_urls = self.start_urls
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('===================')
        news_list = [news for news in json.loads(response.text)['list'] if 'aid' in news.keys()]
        for news in news_list:
            item = ScrapyItem()
            item['title'] = news['title']
            item['link'] = 'https://mil.huanqiu.com/article/' + news['aid']
            item['date_time'] = news['ctime']
            # print(item)
            yield item
        print('====================')
