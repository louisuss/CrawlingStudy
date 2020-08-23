# 다음 주식 정보 가져오기

import json
import urllib.request as req
from fake_useragent import UserAgent
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Fake Header 정보 (가상으로 UserAgent 생성)
ua = UserAgent()
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# 헤더 정보
headers = {
    'User-agent': ua.safari,
    'referer': 'http://finance.daum.net/'
}

# 다음 주식 요청 URL
url = 'http://finance.daum.net/api/search/ranks?limit=10'

# 요청
# Request() 객체 클래스 안에 url, headers 정보 입력
res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# 응답 데이터 확인 (Json Data)
# print('res', res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']

# 중간 확인
# print('중간 확인: \n',rank_json)
# print()

for data in rank_json:
    print('순위: {}, 금액: {}, 회사명: {}'.format(
        data['rank'], data['tradePrice'], data['name']))

# 순위: 1, 금액: 24800, 회사명: 노터스
# 순위: 2, 금액: 328000, 회사명: 셀트리온
# 순위: 3, 금액: 73000, 회사명: 신풍제약
# 순위: 4, 금액: 325000, 회사명: 카카오
# 순위: 5, 금액: 54400, 회사명: 삼성전자
# 순위: 6, 금액: 117500, 회사명: 현대차
# 순위: 7, 금액: 191000, 회사명: SK바이오팜
# 순위: 8, 금액: 69200, 회사명: 일양약품
# 순위: 9, 금액: 106500, 회사명: 셀트리온헬스케어
# 순위: 10, 금액: 175500, 회사명: 씨젠
