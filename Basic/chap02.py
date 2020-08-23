import urllib.request as req
import ssl
from urllib.error import URLError, HTTPError

ssl._create_default_https_context = ssl._create_unverified_context

# 다운로드 경로 및 파일명
path = "/Users/louis/test.jpg"

target = 'http://blogfiles.naver.net/MjAyMDA2MTdfMjQ2/MDAxNTkyMzg1Nzg0ODM3.dl8fSJaSDa77W8Fj8ZkNT2B2nI15erLfzRGjsQvSqQsg.d_tuKjhMeu4G4DeI0873FGc-dvX1yEwFxyskF_UTDHkg.JPEG.noisy002/200617_%C0%CC%C1%F6%C0%BA_4.jpg'

# 예외처리
try:
    # 웹 수신 정보 읽기
    # 다운로드 하지 않고 직접 써줘야 다운로드됨.
    # response로 다른 함수에 넣을 수 있음
    res = req.urlopen(target)

    # 수신 내용
    content = res.read()

    print("----------------")
    # 상태 정보 중간 출력
    print("Header Info \n{} ".format(res.info()))
    print("HTTP Status Code: ".format(res.getcode()))
    print()
    print("----------------")

    with open(path, 'wb') as c:
        c.write(content)


except HTTPError as e:
    print("Failed")
    print("HTTPError Code: ", e.code)
except URLError as e:
    print("Failed")
    print("URLError: ", e.reason)
else:
    print()
    print("SUCCESS")
