from scrapy import Spider
from scrapy.selector import Selector
from ifeng.spiders import IfengItem
from IfengItem import *

class IfengSpider(Spider):
      name = "ifeng"
      start_urls = [
          'http://www.ifeng.com'
      ]
  
      def parse(self,response):
          newslist =Selector(response).xpath('//ul[@class="FNewMTopLis"]/li/a')
          
          for news in newslist:
	      item = IfengItem()
              item['title'] = news.xpath('text()').extract()[0]
              item['url'] = news.xpath('@href').extract()[0]
              self.log('title %s' % news.xpath('text()').extract()[0])
              yield item
