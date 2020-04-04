
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from app.items import AppItem

class Douban(CrawlSpider):
    name = 'douban'
    redis_key = 'douban:start_urls'
    start_urls = ['https://movie.douban.com/top250']

    url = 'https://movie.douban.com/top250'

    def parse(self,response):
        #print response.body
        item = AppItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMoive in Movies:
            title = eachMoive.xpath('//div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMoive.xpath('//div[@class="bd"]/p/text()').extract()
            star = eachMoive.xpath('//div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
            quote = eachMoive.xpath('//div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            #quote可能为空，需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print(nextLink)
            yield Request(self.url + nextLink, callback=self.parse)