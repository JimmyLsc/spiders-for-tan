import datetime

import scrapy

from scrapysina.items import ScrapyItem


class XinhuanetSpider(scrapy.Spider):
    name = 'xinhuanet'
    allowed_domains = ['www.mil.xinhuanet.com']
    start_urls = ['http://www.mil.xinhuanet.com/']
    custom_settings = {
        'ITEM_PIPELINES':{
            'scrapysina.pipelines.ScrapyxinhuanetPipeline': 300
        }
    }

    def start_requests(self):
        start_urls = self.start_urls
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('===================================')
        title_list = response.xpath("//div[@class='tab_box']/div/ul/li/h2/a/text()").extract()
        link_list = response.xpath("//div[@class='tab_box']/div/ul/li/h2/a/@href").extract()
        date_list = response.xpath("//div[@class='tab_box']/div/ul/li/div[@class='time']/text()").extract()
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
        print('===================================')
