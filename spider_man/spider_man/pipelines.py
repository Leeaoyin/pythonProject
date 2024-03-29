# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import openpyxl

from spider_man.items import DoubanItem


class SpiderManPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = 'Top250'
        self.sheet.append(('名称', '评分'))

    def process_item(self, item: DoubanItem, spider):
        self.sheet.append((item['title'], item['score']))
        return item

    def close_spider(self, spider):
        self.wb.save('豆瓣电影数据.csv')
