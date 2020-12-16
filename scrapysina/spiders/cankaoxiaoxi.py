import datetime

import scrapy

from scrapysina.items import ScrapyItem


class CankaoxiaoxiSpider(scrapy.Spider):
    name = 'cankaoxiaoxi'
    allowed_domains = ['mil.cankaoxiaoxi.com']
    start_urls = ['http://mil.cankaoxiaoxi.com/']

    custom_settings = {
        'ITEM_PIPELINES':{
            'scrapysina.pipelines.ScrapycankaoxiaoxiPipeline': 300
        }
    }

    def parse(self, response):
        print('======================================')
        title_list = response.xpath("//div[@class='listCon']/div/div[@class='listBody']/div/div/div[@class='news_pic_info']/p/a/text()").extract()
        link_list = response.xpath("//div[@class='listCon']/div/div[@class='listBody']/div/div/div[@class='news_pic_info']/p/a/@href").extract()
        date_list = response.xpath("//div[@class='listCon']/div/div[@class='listBody']/div/div/div[@class='news_pic_info']/div/span[@class='date_tag']/text()").extract()
        for date, title, link in zip(date_list, title_list, link_list):
            item = ScrapyItem()
            item['link'] = link
            item['date_time'] = date
            item['title'] = title
            month = str(date[5:7])
            day = str(date[8:10])
            today = str(datetime.date.today())
            if month == today[5:7] and day == today[8:10]:
                yield item
        print('======================================')
