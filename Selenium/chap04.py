# Selenium 실습 (4) - 실습 프로젝트(3)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# 엑셀 처리
import xlsxwriter
# 이미지 바이트 처리 - 입출력 바이트로 처리
from io import BytesIO
from urllib.request import Request, urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


chrome_options = Options()
# 크롬 브라우저를 뜨게 안하고 내부적으로 실행하게 하기위해 사용
chrome_options.add_argument("--headless")

# 엑셀 처리 선언
workbook = xlsxwriter.Workbook("/Users/louis/crawling_result.xlsx")

# 워크 시트
worksheet = workbook.add_worksheet()

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome(
    '/Users/louis/Python/AdvancedPython/Crawling/Selenium/chromedriver', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome(
#     '/Users/louis/Python/AdvancedPython/Crawling/Selenium/chromedriver')

# 크롬 브라우저 내부 대기
browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents: {}'.format(browser.page_source))

# 제조사별 더 보기 클릭1
# Explicitly wait
# presence_of_all_elements_located -> 모든 Elements 들이 자리에 나타날 때 까지
# 3초간 기다리되 나타나면 클릭함
WebDriverWait(browser, 3).until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭2
# Implicitly wait
# 전체가 멈추기 때문에 안좋음
# time.sleep(2)
# browser.find_element_by_xpath(
#     '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 선택
WebDriverWait(browser, 2).until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label'))).click()

# 2차 페이지 내용
# print('After Page Contents: {}'.format(browser.page_source))

# 2초간 대기
time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링 할 페이지 수
target_crawl_num = 5

# 엑셀 행 수
ins_cnt = 1

while cur_page <= target_crawl_num:
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('********** Current Page: {} *************'.format(cur_page))

    # 필요 정보 추출
    for v in pro_list:
        # 임시출력
        # print(v)

        if not v.find('div', class_="ad_header"):
            # 상품명, 가격
            prod_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = v.select('p.price_sect > a')[0].text.strip()

            # 일부 이미지는 data-original key가 없음
            s = ''
            if v.select('a.thumb_link > img')[0].has_attr('data-original'):
                s = v.select('a.thumb_link > img')[0]['data-original']
            else:
                s = v.select('a.thumb_link > img')[0]['src']
            # 이미지 요청 후 바이트 변환
            # headers 정보 안주면 403 에러뜸
            # raise HTTPError(req.full_url, code, msg, hdrs, fp)
            # urllib.error.HTTPError: HTTP Error 403: Forbidden
            r = Request(s, headers={'User-Agent': 'Mozilla/5.0'})
            img_data = BytesIO(urlopen(r).read())

            # 엑셀 저장(텍스트)
            worksheet.write('A%s' % ins_cnt, prod_name)
            worksheet.write('B%s' % ins_cnt, prod_price)

            # 엑셀 저장(이미지)
            worksheet.insert_image('C%s' % ins_cnt, prod_name, {
                                   'image_data': img_data})

            ins_cnt += 1

    print()

    # 페이지 별 스크린 샷 저장
    browser.save_screenshot(
        "/Users/louis/target_page{}.png".format(cur_page))

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawling Successed')
        break

    # 페이지 이동 클릭
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # BeautifulSoup 인스턴스 삭제
    del soup

    # 3초간 대기
    time.sleep(2)


# 브라우저 종료
browser.close()

# 엑셀 파일 닫기
# 안닫으면 파일 생성 안됨
workbook.close()
