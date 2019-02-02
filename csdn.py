# -*- coding: utf-8 -*-
# scrapy shell https://blog.csdn.net/s98
import scrapy
from scrapy.loader import ItemLoader
from ..items import Test1Item

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://blog.csdn.net/s98//article/list/1']
    next_url = ['https://blog.csdn.net/s98//article/list/1']

    def __init__(self):
        for x in range(1,16):
            x=x+1
            self.next_url.append('https://blog.csdn.net/s98//article/list/'+str(x))


    def parse(self, response):
        #处理下一页
        for i in self.next_url:
            #print('***************'+i+'********')
            yield scrapy.Request(url=i,callback=self.parse)

        #解析处理每一页内容，送给parse_detail处理
        num = len(response.xpath('//*[@class="article-list"]//h4/a/@href').extract())
        for i in range(1,num + 1):
            url =  response.xpath('//*[@class="article-list"]//h4/a/@href').extract()[i]
            yield scrapy.Request(url,callback=self.parse_detail)

    def parse_detail(self,response):
        title = response.xpath('//*[@class="title-article"]/text()').extract()[0]
        time = response.xpath('//*[@class="time"]/text()').extract()[0]
        item= Test1Item()
        item['title']= title
        item['time'] = time
        yield item
