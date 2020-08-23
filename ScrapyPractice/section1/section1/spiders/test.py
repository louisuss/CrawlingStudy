import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        param : response
        return : Title Text
        """

        # 2가지 (CSS_Selector, XPath)
        # getall() <-> get(), extract() <-> extract_first()
        # 가져올 때 사용

        # css
        # ::a -> a 태그 텍스트만 가져옴
        # 출력 옵션 :
        # -o 파일명, 확장자, -t 파일 타입(json, jsonlines, jl, csv, xml, marshal, pickle)
        # for text in response.css('div.post-header h2 a::text').getall():
        #     # return Type : Request, BaseItem, Dictionary, None
        #     yield {
        #         'title': text
        #     }

        # scrapy crawl test -o result.jl -t jsonlines
        # scrapy crawl test -o result.csv -t csv

        # XPath
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            yield {
                'number': i,
                'text': text
            }
