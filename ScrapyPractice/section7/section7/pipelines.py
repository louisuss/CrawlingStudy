# 파이프라인 실습(1)
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, SMS 전송, 메일 전송
from scrapy.exceptions import DropItem


class TestSpiderPipeline:
    # 최초 1회만 실행
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started.')

    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. Rank Below 40.')

    # 마지막 1회만 실행
    def close_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Finished.')
