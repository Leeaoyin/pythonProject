import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from spider_man.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}')


    def parse(self, response):
        pass
