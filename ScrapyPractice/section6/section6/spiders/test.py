import scrapy

# Scrapy 환경 설정
# 실행 방법
# 1. 커맨드 라인 실행 -> scrapy crawl 크럴러명 -s(--set) <NAME>=<VALUE>
# 2. Spider 실행 시 직접 지정
# 3. Settings.py에 지정 -> 추천
# 4. 서브 명령어 (신경X)
# 5. 글로벌 설정: scrapy.settings.default_settings


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    # 2. Spider 환경 설정
    # custom_settings = {
    #     'DOUNLOAD_DELAY': 3
    # }

    def parse(self, response):
        for i, v in enumerate(response.xpath('//div[@class="post-summary-content"]').css('div.post-excerpt-container > h3 > a::text').getall(), 1):
            yield dict(num=i, headline=v)
