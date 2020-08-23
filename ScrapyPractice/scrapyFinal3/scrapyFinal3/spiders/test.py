# URL 규칙 주면 링크 순회
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItems
import scrapy


class NewsSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['news.daum.net/breakingnews/']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    # \d -> 1자리 숫자
    # \d+ -> 숫자가 상관 없음
    # \d$ -> $정규 표현식의 끝 표현
    # page=\d$ : 1자리 수
    # page=\d+ : 연속, follow=True
    rules = [
        # Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d+'),
        #      callback='parse_headline', follow=True),
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'),
             callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Response URL: %s' % response.url)

        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # URL : 신문 기사 URL
            # 페이지 안에 있는 신문 기사 리스트
            article_url = url.css(
                'strong > a::attr(href)').extract_first().strip()
            # 요청
            # meta 로 자식 메소드에 데이터 전달
            yield scrapy.Request(article_url, callback=self.parse_child, meta={'parent_url': response.url})

    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        self.logger.info('--------------------------')
        self.logger.info('Response From Parent URL : %s' %
                         response.meta['parent_url'])
        # 신문기사 하나하나의 URL
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status: %s' % response.status)
        self.logger.info('--------------------------')

        # 헤드라인
        headline = response.css('h3.tit_view::text').extract_first().strip()
        # 본문
        c_list = response.css('div.article_view > p::text').extract()

        contents = ''.join(c_list).strip()

        yield ArticleItems(headline=headline, contents=contents, parent_lenk=response.meta['parent_url'], article_link=response.url)
