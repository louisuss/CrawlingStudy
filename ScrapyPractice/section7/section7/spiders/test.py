import scrapy
from ..items import SiteRankItems


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['http://alexa.com/topsites/']

    def parse(self, response):
        """
        param: response
        return: SiteRankItems
        """
        # 클래스 이름이 class="listing table" -> 띄어쓰기 되있으므로 .두번
        for p in response.css('div.listings.table > div.tr.site-listing'):
            # 아이템 객체 생성
            item = SiteRankItems()
            item['rank_num'] = p.xpath('div[@class="td"]/text()').get()
            # 클래스 이름이 class="listing table"
            item['site_name'] = p.xpath(
                'div[@class="td DescriptionCell"]/p/a/text()').get()
            # 클래스 이름이 여러개가 같은 경우
            item['daily_time_site'] = p.xpath(
                'div[@class="td right"]/p/text()').getall()[0]
            item['daily_page_view'] = p.xpath(
                'div[@class="td right"]/p/text()').getall()[1]
            yield item
