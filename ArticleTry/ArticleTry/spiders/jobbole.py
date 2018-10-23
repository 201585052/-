# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        # xpath是可以通过开发者工具获取的
        re_selector = response.xpath('/html/body/div[3]/div[3]/div[1]/div[1]')
        # re_selector返回的并不是个node节点，而是一个选择器，方便开发者进一步对选择器进行开发（如node中的node的选取）
        pass
