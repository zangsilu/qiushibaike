# -*- coding: utf-8 -*-
import scrapy
from qiushibaike.items import QiushibaikeItem

class Spider(scrapy.Spider):
    name = 'qiushibaike'
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    def parse(self, response):
        list = response.xpath('//*[@id="content-left"]/div')
        for info in list:
            item = QiushibaikeItem()
            username = info.xpath('.//div[1]/a[2]/h2/text()').extract_first()
            if username:
                item['username'] = username.replace('\n', '')
                item['avatar'] = response.urljoin(info.xpath('.//div[1]/a[1]/img/@src').extract_first())
                item['content'] = info.xpath('.//a[1]/div/span[1]/text()').extract_first().replace(' ','').replace('\n','')
                contentImage = info.xpath('.//div[2]/a/img/@src').extract_first()
                if contentImage:
                    item['contentImage'] = response.urljoin(contentImage)
                else:
                    item['contentImage'] = ''
                item['nextPage'] = response.urljoin(response.xpath("//ul[@class='pagination']/li[last()]/a/@href").extract_first())
                yield item

        nextPage = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").extract_first()
        if nextPage:
            nextUrl = response.urljoin(nextPage)
            yield scrapy.Request(nextUrl,self.parse)

