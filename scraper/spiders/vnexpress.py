# -*- coding: utf-8 -*-
import scrapy
from scraper.items import ScraperItem
import lxml

class SohoaVnexpressNet(scrapy.Spider):
    name = 'test'
    allowed_domains = ["vnexpress.net"]

    counter = 0
    max_page = 100
    index = 0

    def start_requests(self):
        urls = []
        base_url = 'http://vnexpress.net/tin-tuc/'
        articles = ['the-gioi',
                    'thoi-su',
                    'phap-luat',
                    'khoa-hoc',
                    'giao-duc',
                    ]

        for item in articles:
            self.counter = 0
            while self.counter < self.max_page:
                self.counter += 1
                urls.append(base_url + item + '/page/' + str(self.counter) + '.html')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_news)

    def parse_news(self, response):

        ARTICLE_SELECTOR = '//article[contains(@class,"list_news")]'
        for row in response.xpath(ARTICLE_SELECTOR).extract():
            if row.strip():
                row = lxml.html.fromstring(row)
                # title = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/text()')), "").strip()
                # url = next(iter(row.xpath('//h3[contains(@class,"title_news")]//a/@href')), "").strip()
                description = next(iter(row.xpath('//h4[contains(@class,"description")]/text()')), "").strip()
				
                # if title and description and url:
                if description:
                    # self.index += 1
                    item = ScraperItem()
                    # item['id'] = str(self.index)
                    item['description'] = description
                    # item['title'] = title
                    # item['url'] = url
                    yield item

