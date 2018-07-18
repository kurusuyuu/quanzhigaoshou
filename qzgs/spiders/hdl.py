# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from qzgs.items import QzgsItem


class HdlSpider(CrawlSpider):
    name = 'hdl'
    allowed_domains = ['www.biquge.com.tw']
    start_urls = ['http://www.biquge.com.tw/0_32/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.biquge.com.tw/0_32/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = QzgsItem()
        item['title'] = sel.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/h1').extract()
        contents = response.selector.xpath('//*[@id="content"]').extract()
        i = ''
        for content in contents:
            i += content
        m = re.compile(r'(\r\n\xa0\xa0\xa0\xa0)|(\r\n)|(/\xa0\xa0\xa0\xa0)')
        contents = m.sub('',i)
        item['content'] = contents

        yield item


