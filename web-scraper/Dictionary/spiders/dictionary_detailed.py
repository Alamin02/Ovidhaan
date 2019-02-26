# -*- coding: utf-8 -*-
import scrapy


class DictionaryDetailedSpider(scrapy.Spider):
    name = 'dictionary_detailed'
    allowed_domains = ['english-bangla.com']
    start_urls = ['http://english-bangla.com/browse/']

    def parse(self, response):
        letter_urls = response.css('div.a-z > a::attr(href)').extract()

        for letter in letter_urls:
            yield scrapy.Request(url=letter, callback=self.parse_letter)

    def parse_letter(self, response):
        word_url_list = response.css('div#cat_page > ul > li > a::attr(href)').extract()

        for word_url in word_url_list:
            yield scrapy.Request(url=word_url, callback=self.parse_word)

        next_page_url = response.css('div.pagination > a[rel=next]::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse_letter)

    @staticmethod
    def parse_word(response):
        word = response.css('span#speak.word::text').extract_first().strip()
        meaning = response.css('span.format1::text').extract_first()
        yield {
            'word': word,
            'meaning': meaning
        }

