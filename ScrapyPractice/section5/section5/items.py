# 1. 수집 데이터를 일관성있게 관리 가능
# 2. 데이터를 사정형(Dict)로 관리, 오타 방지
# 3. 추후 가공 및 DB 저장 용이

import scrapy


class ItArticle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 제목
    title = scrapy.Field()
    # image URL
    img_url = scrapy.Field()
    # contents
    contents = scrapy.Field()
