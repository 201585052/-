# -*- coding: utf-8 -*-
import scrapy
import re
import datetime

from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader
from ArticleTry.items import JobBoleArticleItem
from ArticleTry.spiders.common import get_md5


# xpath是可以通过开发者工具获取的
# 如果是自己手动写xpath有问题的话去网页源代码里看，开发者工具里是js操作后的结果
# 以下是css套路
# reponse.css(".entry-header h1::text").extract() 
# re_selector返回的并不是个node节点，而是一个选择器，方便开发者进一步对选择器进行开发（如node中的node的选取）


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''
        1、获取文章列表中的文章url并交给scrapy下载后解析函数进行具体解析
        2、获取下一页的url并交给scrapy下载完成后给parse    
        '''
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url":image_url}, callback=self.parse_detail)
        # 提取下一页并交给scrapy进行下载
        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")# 连起来写是让类加起来
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)


    def parse_detail(self, response):
        # 提取文章的具体字段

        article_item = JobBoleArticleItem()
        '''
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

        #通过css选择器提取字段
        front_image_url = response.meta.get("front_image_url", "")  #文章封面图
        title = response.css(".entry-header h1::text").extract()[0]
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·","").strip()
        praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0
        
        comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0
        
        content = response.css("div.entry").extract()[0]
        
        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        
        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        try:
            create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        except Exception as e:
            create_date = datetime.datetime.now().date()
        article_item["create_date"] = create_date
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = praise_nums
        article_item["comment_nums"] = comment_nums
        article_item["fav_nums"] = fav_nums
        article_item["tags"] = tags
        article_item["content"] = content
        yield article_item
        
