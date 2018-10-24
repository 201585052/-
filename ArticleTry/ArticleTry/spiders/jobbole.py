# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.http import Request


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # xpath是可以通过开发者工具获取的
        # 如果是自己手动写xpath有问题的话去网页源代码里看，开发者工具里是js操作后的结果
        # 以下是css套路
        # reponse.css(".entry-header h1::text").extract() 
        # re_selector返回的并不是个node节点，而是一个选择器，方便开发者进一步对选择器进行开发（如node中的node的选取）
        '''
        1、获取文章列表中的文章url并交给scrapy下载后解析函数进行具体解析
        2、获取下一页的url并交给scrapy下载完成后给parse    
        '''
        post_urls = response.css("#archive .floated-thumb .post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            Request(url = post_url)
            print (post_url)




        '''
        re_selector = response.xpath('//*[@id="post-114413"]/div[1]/h1/text()')
        title = response.xpath("//*[@id='post-114413']/div[1]/h1/text()").extract_first("") # 这么写有利于防止数组越界报错，源码在init.py里
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
        '''
        pass
        
