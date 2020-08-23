# BeautifulSoup 사용 스크래핑(2) - 이미지 다운로드

import os
import urllib.parse as rep
import ssl
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# urlopen error
# urlretriect error
# 의존성 추가
# context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context


# Header 정보 초기화
opener = req.build_opener()

# User-Agent 정보
# ie -> user agent를 fake로 랜덤으로 생성
# opener.addheaders = [('User-agent', UserAgent().ie)]

# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL (크롬 개발자 도구)
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

# 검색어
quote = rep.quote_plus('아이유')
# URL 완성
url = base + quote

# 요청 URL 확인
print('Request URL: {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "/Users/louis/Imagedown/"

# 폴더 생성 예외 처리(문제 발생 시 프로그램 종료)
try:
    # 기본 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        # 없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
    print("Folder creation failed.")
    print("folder name: {}".format(e.filename))

    # 런타임 에러
    raise RuntimeError("System Exit!")
else:
    # 폴더 생성이 되었거나, 존재할 경우
    print("folder is created")

soup = BeautifulSoup(res, "html.parser")

# print(soup.prettify())

# select 사용
# BeautifulSoup 강점
img_list = soup.select('div.img_area > a.thumb._thumb > img')

# find_all 사용
# img_list2 = soup.find_all('a', class_="thumb _thumb")
# print(img_list2)
# for v in img_list2:
#     img_t = v.find('img')
#     print(img_t.attrs['data-source'])

for i, img in enumerate(img_list, 1):
    # 속성 확인
    # print()
    # print(img['data-source'], i)

    # 저장 파일명 및 경로
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
    # print(fullFileName)

    # 다운로드 요청(URL, 다운로드 경로)
    req.urlretrieve(img['data-source'], fullFileName)

# 다운로드 완료 시 출력
print('Success')
