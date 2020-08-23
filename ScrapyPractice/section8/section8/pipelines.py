# 파이프라인 실습(2)
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, SMS 전송, 메일 전송
from scrapy.exceptions import DropItem
import csv
import xlsxwriter


class TestSpiderPipeline:
    # 초기화 메서드
    def __init__(self):
        # 엑셀 처리 선언
        self.workbook = xlsxwriter.Workbook('/Users/louis/result_excel.xlsx')
        # CSV 처리 선언 (a(append), w(write) 옵션 변경)
        self.file_opener = open('/Users/louis/result_csv.csv', 'w')
        self.csv_writer = csv.DictWriter(self.file_opener, fieldnames=[
                                         'rank_num', 'site_name', 'daily_time_site', 'daily_page_view', 'is_pass'])
        # 워크시트
        self.worksheet = self.workbook.add_worksheet()
        # 삽입수
        self.rowcount = 1

    # 최초 1회만 실행
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started.')

    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True

            # 엑셀 저장
            # item['rank_num'] 도 가능하지만 없으면 에러, get으로 받으면 없을 시 None 반환해서 더 안전
            self.worksheet.write('A%s' % self.rowcount, item.get('rank_num'))
            self.worksheet.write('B%s' % self.rowcount, item.get('site_name'))
            self.worksheet.write('C%s' % self.rowcount,
                                 item.get('daily_time_site'))
            self.worksheet.write('D%s' % self.rowcount,
                                 item.get('daily_page_view'))
            self.worksheet.write('E%s' % self.rowcount, item.get('is_pass'))
            self.rowcount += 1

            # CSV 저장
            # item -> dict 형태기 때문에 바로 넣어주면 됨
            self.csv_writer.writerow(item)

            return item
        else:
            raise DropItem(f'Dropped Item. Rank Below 40.')

    # 마지막 1회만 실행
    def close_spider(self, spider):
        # 엑셀 파일 닫기
        self.workbook.close()
        # CSV 파일 닫기
        self.file_opener.close()
        spider.logger.info('TestSpider Pipeline Finished.')
