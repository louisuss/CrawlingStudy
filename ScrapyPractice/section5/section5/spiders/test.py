import scrapy
from ..items import ItArticle


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['computerworld.com/news']
    start_urls = ['https://www.computerworld.com/news']

    def parse(self, response):
        """
        param: response
        return: Request -> 재귀형식
        """

        for url in response.css('div.main-col > div.river-well > div.post-cont > h3 > a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """
        param: response
        return: Items
        """
        item = ItArticle()
        item['title'] = response.xpath('//header[@id="banner"]/h1').get()
        item['img_url'] = response.xpath(
            '//div[@class="constrain-970"]/div/figure/img/@data-original').get()
        item['contents'] = ''.join(response.xpath(
            '//div[@id="drr-container"]/p/text()').getall())

        # print(dict(item))
        # print(dir(dict(item)))

        yield item
