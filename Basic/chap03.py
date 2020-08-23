# GET 방식 데이터 통신 (1)

import urllib.request
from urllib.parse import urlparse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 기본 요청1 (encar)
url = "http://www.encar.com"

mem = urllib.request.urlopen(url)

# 여러 정보 출력
print('Type: {}'.format(type(mem)))
print('GETURL: {}'.format(mem.geturl()))
print('Status: {}'.format(mem.status))
print('GETCODE: {}'.format(mem.getcode()))
print('Headers: {}'.format(mem.getheaders()))
print('READ: {}'.format(mem.read(100).decode('UTF-8')))
# 중요
# URL 을 파싱해서 도메인 부분, 프로토콜 부분, 쿼리 부분 분리
print('PARSE: {}'.format(urlparse(url+'?test=test')))
print('PARSE: {}'.format(urlparse(url+'?test=test').query))

# 기본 요청2(ipify)
API = 'https://api.ipify.org'

# GET 방식 Parameter
values = {
    'format': 'json'
}

print('Before param: {}'.format(values))
params = urllib.parse.urlencode(values)
print('After param: {}'.format(params))

# 요청 URL 생성
URL = API + "?" + params
# {"ip":"182.217.155.231"} -> ip 주소 출력
print("요청 URL = {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이커 디코딩
text = data.decode('UTF-8')
print('Response: {}'.format(text))
