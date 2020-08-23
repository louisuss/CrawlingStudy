# requests 사용 스크래핑(1) - Session
# 클라이언트는 서버측에서 이 클라이언트가 정상적으로 접근을 해서
# 내가 주는 정보를 수신해가는지 확인하기 위해 쿠키나 헤더정보를 확인


import requests

# 세션 활성화
# s = requests.Session()
# r = s.get('https://www.naver.com')

# # 수신 데이터
# # print(r.text)

# # 수신 상태 코드
# print('Status Code: {}'.format(r.status_code))

# # 확인
# # 주로 조건문에서 많이 활용
# print('Ok?: {}'.format(r.ok))

# # 세션 비활성화
# s.close()

# 쿠키 return
# https://httpbin.org/

s = requests.Session()

# 쿠키 return
# 서버가 확인하고 그대로 리턴
# {
#     "cookies": {
#         "name": "kim"
#     }
# }
r1 = s.get('https://httpbin.org/cookies', cookies={'name':'kim'})
print(r1.text)

# 쿠키 Set
# 쿠키를 서버쪽에 저장할 때 사용
r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'kim2'})
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
# UserAgent - 서버에서 클라이언트를 식별할 때 가장 중효하게 헤더 정보에서 보는 속성 값
headers = {'user-agent':'chrome'}

# Header 정보 전송
r3 = s.get(url, headers=headers, cookies={'name': 'kim3'})
print(r3.text)

s.close()

# with문 사용 (권장) -> 파일, DB, HTTP
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)
    # with 문 끝나면 자동적으로 리소스 반환됨

