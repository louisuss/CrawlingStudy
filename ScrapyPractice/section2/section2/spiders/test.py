# scrapy crawl test - o test_file.jl -> 터미널에서 jl 파일 생성해서 체크
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        param : response
        return : Request
        """
        # href 중 https://--- 같은 공통 부분은 생략된 상대경로인 경우가 있어서 체크 필요 -> 절대경로 필요
        for url in response.css('div.post-item > div > a::attr("href")').getall():
            # print(url)

            # url 바로 사용 보다 urljoin 사용

            yield scrapy.Request(response.urljoin(url), self.parse_title)

    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        param : response
        return : Text
        """
        contents = response.css(
            'div.post-body > span > p::text').extract()[:4]  # getall()
        # print(contents)
        # list 형식을 문자열 형식으로 풀음 ''.join(list)
        yield {'contents': ''.join(contents)}
