import datetime

import scrapy

from scrapysina.items import ScrapyItem


class SastindSpider(scrapy.Spider):
    name = 'sastind'
    allowed_domains = ['http://www.sastind.gov.cn']
    start_urls = ['http://www.sastind.gov.cn/n112/n117/index.html']
    custom_settings = {
        'ITEM_PIPELINES':{
            'scrapysina.pipelines.ScrapysastindPipeline': 300
        }
    }

    def start_requests(self):
        start_urls = self.start_urls
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('=================================')
        link_list = response.xpath("//span/table[2]/tr/td/table/tr/td[2]/a/@href").extract()
        title_list = response.xpath("//span/table[2]/tr/td/table/tr/td[2]/a/text()").extract()
        date_list = response.xpath("//span/table[2]/tr/td/table/tr/td[3]/text()").extract()
        for date, title, link in zip(date_list, title_list, link_list):
            item = ScrapyItem()
            item['link'] = link
            item['date_time'] = date
            item['title'] = title
            month = str(date[1:3])
            day = str(date[4:6])
            today = str(datetime.date.today())
            if month == today[5:7] and day == today[8:10]:
                yield item
        print('=================================')


