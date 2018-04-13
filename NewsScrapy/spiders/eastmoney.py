import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from NewsScrapy.items import EastmoneyScrapyItem

class Myspider(scrapy.Spider):
     name = 'eastmoney'
     allowed_domains = ['eastmoney.com']

     def start_requests(self):
         yield Request('http://stock.eastmoney.com/news/cscjh.html',self.parse)

     def parse(self, response):
        print(response.text)