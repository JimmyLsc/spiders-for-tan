import datetime

import scrapy

from scrapysina.items import ScrapyItem


class DempSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['http://mil.news.sina.com.cn']
    start_urls = ['http://mil.news.sina.com.cn/roll/index.d.html?cid=57918',
                    'http://mil.news.sina.com.cn/roll/index.d.html?cid=57919/',
                  'http://mil.news.sina.com.cn/roll/index.d.html?cid=234399',
                  'http://mil.news.sina.com.cn/roll/index.d.html?cid=234400']

    custom_settings = {
        'ITEM_PIPELINES':{
            'scrapysina.pipelines.ScrapysinaPipeline': 300
        }
    }

    def start_requests(self):
        start_urls = self.start_urls
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        print('=================================')
        link_list = response.xpath("//ul[@class='linkNews']/li/a/@href").extract()
        date_list = response.xpath("//ul[@class='linkNews']/li/span/text()").extract()
        title_list = response.xpath("//ul[@class='linkNews']/li/a/text()").extract()
        for date, title, link in zip(date_list, title_list, link_list):
            item = ScrapyItem()
            item['link'] = link
            item['date_time'] = date
            item['title'] = title
            month = str(date[1:3])
            day = str(date[4:6])
            today = str(datetime.date.today())
            if month == today[5:7] and day == today[8:10]:
                # print(item)
                yield item
        print('=================================')


