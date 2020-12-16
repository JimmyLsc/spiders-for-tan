# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter


class ScrapysinaPipeline:

    def __init__(self):
        self.file = open('./files/sina.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print(item)


    def closs_item(self, spider):
        self.file.close()


class ScrapysastindPipeline:

    def __init__(self):
        self.file = open('./files/sastind.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print(item)


    def closs_item(self, spider):
        self.file.close()

class ScrapyhuanqiuPipeline:

    def __init__(self):
        self.file = open('./files/huanqiu.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print(item)


    def closs_item(self, spider):
        self.file.close()

class ScrapyxinhuanetPipeline:

    def __init__(self):
        self.file = open('./files/xinhuanet.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print(item)


    def closs_item(self, spider):
        self.file.close()

class ScrapycankaoxiaoxiPipeline:

    def __init__(self):
        self.file = open('./files/cankaoxiaoxi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print(item)


    def closs_item(self, spider):
        self.file.close()

