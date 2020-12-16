import scrapy


class IfengSpider(scrapy.Spider):
    name = 'ifeng'
    allowed_domains = ['https://mil.ifeng.com/']
    start_urls = ['https://mil.ifeng.com/shanklist/original/14-35084-', 'https://mil.ifeng.com/shanklist/14-35083-']

    def start_requests(self):
        start_urls = self.start_urls
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        title_list = response.xpath("//*[@id='root']/div[5]/div[1]/div/ul/li[1]/div/h2/a").extract()
        print(title_list)
        pass

