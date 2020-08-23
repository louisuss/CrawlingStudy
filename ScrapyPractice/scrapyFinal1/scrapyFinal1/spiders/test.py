# URL 규칙 주면 링크 순회
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NewsSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['news.daum.net']
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
             callback='parse_headline'),
    ]

    def parse_headline(self, response):
        # URL 로깅
        self.logger.info('Response URL: %s' % response.url)

        for m in response.css('ul.list_news2.list_allnews > li > div'):
            # 헤드라인
            headline = m.css('strong > a::text').extract_first().strip()
            # 본문 20글자
            contents = m.css('div > span::text').extract_first().strip()

            yield {'headline': headline, 'contents': contents}
