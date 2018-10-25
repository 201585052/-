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


