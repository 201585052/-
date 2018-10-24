# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114413/']

    def parse(self, response):
        # xpath是可以通过开发者工具获取的
        # 如果是自己手动写xpath有问题的话去网页源代码里看，开发者工具里是js操作后的结果
        re_selector = response.xpath('//*[@id="post-114413"]/div[1]/h1/text()')
        title = response.xpath("//*[@id='post-114413']/div[1]/h1/text()").extract()[0]
        create_date = response.xpath("//*[@id='post-114413']/div[2]/p/text()").extract()[0].strip().replace('·','').rstrip()
        praise_nums = response.xpath("//*[@id='114413votetotal']/text()").extract()[0]
        fav_nums = response.xpath("//*[@id='post-114413']/div[3]/div[9]/span[2]/text()").extract()[0]
        match_re = re.match(".*(\d+).*",fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        comen_nums = comen_nums = response.xpath("//*[@id='post-114413']/div[3]/div[9]/a/span/text()").extract()[0]
        match_re = re.match(".*(\d+).*",comen_nums)
        if match_re:
            comen_nums = match_re.group(1)
        else:
            comen_nums = 0
        content = response.xpath("//div[@class = 'entry']").extract()
        print ("brelly liaoliao")
        print (comen_nums)
        # re_selector返回的并不是个node节点，而是一个选择器，方便开发者进一步对选择器进行开发（如node中的node的选取）
        pass
