# Selenium 실습 (2) - 실습 프로젝트(1)

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
# 크롬 브라우저를 뜨게 안하고 내부적으로 실행하게 하기위해 사용
chrome_options.add_argument("--headless")

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

time.sleep(2)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 소스코드 정리
# print(soup.prettify())

# 메인 상품 리스트 선택
pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')


# 상품 리스트 확인
# print(pro_list)

# 필요 정보 추출
for v in pro_list:
    # 임시출력
    # print(v)

    if not v.find('div', class_="ad_header"):
        # 상품명, 이미지, 가격
        print(v.select('p.prod_name > a')[0].text.strip())

        # 일부 이미지는 data-original key가 없음
        if v.select('a.thumb_link > img')[0].has_attr('data-original'):
            print(v.select('a.thumb_link > img')[0]['data-original'])
        else:
            print(v.select('a.thumb_link > img')[0]['src'])
        print(v.select('p.price_sect > a')[0].text.strip())
    print()

# 브라우저 종료
browser.close()
