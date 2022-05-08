import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from spider_man.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/']

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}')


    def parse(self, response):
        select = Selector(response)
        item = DoubanItem()
        for x in range(1, 26):
            item['title'] = select.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{x}]/div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            item['score'] = select.xpath(f'//*[@id="content"]/div/div[1]/ol/li[{x}]/div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            yield item
