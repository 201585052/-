# 日记

# 技术栈

初步的想法是因为可能会用到爬虫，而且是做数据相关的，所以主语言是选的python吧，想法是Scrapy爬虫爬数据->whoosh做索引->Django写后台->前端展现

## 小坑

* python 3.7中将async设为关键字
* response.css 和cheerio同出一辙嘛,但还是先学了xpath
* 这叫个巨坑了 改mysql的字符编码集  :    https://blog.csdn.net/benjamin_whx/article/details/44747653
* :w !sudo tee %   -> vim 强制保存

```sql
create table jobbole_article(
    title varchar(200) not null,
    create_date datetime,
    url varchar(300) not null,
    -- url_object_id varchar(50) not null primary key,
    -- front_image_url varchar(300),
    -- front_image_path varchar(300),
    -- comment_nums int(11) not null default 0,
    fav_nums int(11) not null default 0
    -- praise_nums int(11) not null default 0,
    -- tags varchar(100),
    -- content longtext
)DEFAULT CHARSET=utf8;
```

* 异步存数据到mysql的步骤中出现了莫名奇妙的错误

## 知识随笔

* JSONView 好像还不错的插件

* 因为时间的缘故只能先学习了。。。。。。只能交大牛的作业了，不过这里的话scrapy、mysql、redis分布式、Django等东西还是值得学的，至少要把材料看完orz

* crawlera(代理)

* 洋葱网络(tor)、高匿IP

* 云打码（等在线打码平台）

* Nosql文档数据库也是区分于关系型数据库的Mysql，话说在研究分布式的时候也是用到了redis哈，保存在内存中，很快。Redis和MongoDB也是Nosql类型中的典型代表

* 倒排索引与倒排列表

* es的crud主要用head（可视化查询）和kibana（类似编译器)