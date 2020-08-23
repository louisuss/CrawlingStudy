import datetime
import sqlite3
from scrapy.exceptions import DropItem


class NewsSpiderPipeline:

    # 초기화 메서드
    def __init__(self):
        # DB 설정(자동 커밋 -> isolation_level=None)
        self.conn = sqlite3.connect('/Users/louis/db', isolation_level=None)
        # DB 연결
        self.c = self.conn.cursor()

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('NewsSpider Pipeline Started.')
        self.c.execute('CREATE TABLE IF NOT EXISTS NEWS_DATA(id INTEGER PRIMARY KEY AUTOINCREMENT, headline text, contents text, parent_link  text, article_link text, crawled_time text)')

    # item 건수 별 실행

    def process_item(self, item, spider):
        if not item.get('contents') is None:
            crawled_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 크롤링 시간 필드 추가
            item['crawled_time'] = crawled_time
            # 데이터 -> DB 삽입
            self.c.execute('INSERT INTO NEWS_DATA(headline, contents, parent_link, article_link, crawled_time) VALUES(?, ?, ?, ?, ?);', (item.get(
                'headline'), item.get('contents'), item.get('parent_link'), item.get('article_link'), item.get('crawled_time')))  # tuple(item[k] for k in item.keys())

            # 로그
            spider.logger.info('Item to DB inserted.')
            # 결과 리턴
            return item
        else:
            raise DropItem('Dropped Item. This contents is empty.')

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('NewsSpider Pipeline Stopped.')
        # 커밋
        self.conn.commit()
        # 연결 해제
        self.conn.close()
