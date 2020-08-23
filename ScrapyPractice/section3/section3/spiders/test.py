import scrapy

# 참고 하지만 제공되는 logger 사용이 더 유용
# import logging

# logger = logging.getLogger('MyLogger')


# 스파이더 종류: CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = 'test'
    # 여기 있는 사이트만 허용
    allowed_domains = ['blog.scrapinghub.com',
                       'naver.com', 'daum.net']
    # 해당 사이트 방문
    # 멀티 도메인 실행 방법1
    start_urls = ['http://blog.scrapinghub.com/',
                  'https://naver.com', 'https://daum.net']

    # 사용자 시스템 설정 (settings.py)
    custom_settings = {
        'DOWNLOAD_DELAY': 1
        # 'COOKIES_ENABLED': True
    }
    # 멀티 도메인 실행 방법2
    # 함수를 나눠 해당 사이트별로 특정 기능 처리 가능
    # Request 각자 지정

    # def start_requests(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self.parse1)
    #     yield scrapy.Request('https://naver.com', self.parse2)
    #     yield scrapy.Request('https://daum.net', self.parse3)

    # parse를 나눌 수도 있고 parse로 해서 if문으로 분기 처리해서 주로 사용
    # def parse1(self, response):
    #     pass
    # def parse2(self, response):
    #     pass
    # def parse3(self, response):
    #     pass

    def parse(self, response):
        # print문 보다 활용도가 좋음
        # loger.info()
        self.logger.info('Response URL: %s' % response.url)
        self.logger.info('Response Status: %s' % response.status)

        if response.url.find('scrapinghub'):
            # 원하는 데이터 출력
            # response.css('')
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
