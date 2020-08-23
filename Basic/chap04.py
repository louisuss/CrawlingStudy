# 기본 스크래핑 실습
# GET 방식 데이터 통신(2) - RSS
# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001

import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 행정 안전부 RSSAPI URL
API = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# [{'ctxCd': 1001}, {'ctxCd': 1012}, {'ctxCd': 1013}, {'ctxCd': 1014}]
# print(params)

# 연속해서 4회 요청
for c in params:
    # 파라미터 출력
    # print(c)
    # URL 인코딩
    param = urllib.parse.urlencode(c)
    
    # URL 완성
    url = API + "?" + param

    # URL 출력
    print('URL: {}'.format(url))

    # 요청
    res_data = urllib.request.urlopen(url).read()
    # print(res_data)

    # 수신 후 디코딩
    # 수신 후 정확한 출력값 확인위해 사용
    contents = res_data.decode('UTF-8')

    # 출력
    print('--------------')
    print(contents)
