# requests 사용 스크래핑(3) - Rest API

# Rest API: GET, POST, DELETE, PUT: UPDATE, REPLACE(FETCH: UPDATE, MODIFY)
# 중요: URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET: www.movies.com/movies - 영화를 전부 조회
# GET: www.movies.com/movies/:id - 아이디인 영화를 조회
# POST: www.movies.com/movies - 영화 생성
# PUT: www.movies.com/movies - 영화 수정
# DELETE: www.movies.com/movies - 영화 삭제

import requests

# GET
# 세션 활성화
s = requests.Session()

# EX1
r = s.get('https://api.github.com/events')

# 수신 상태 체크
# 에러가 나면 예외 발생하고 예외처리 하고 끝남
r.raise_for_status()

# 출력
# print(r.text)

# EX2
# 쿠키 설정 (정석)
# RequestsCookieJar() 에 데이터 속성 값 넣음
jar = requests.cookies.RequestsCookieJar()

# 쿠키 삽입
jar.set('name', 'niceman', domain='httpbin.org', path='/cookies')

# 요청
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
print(r.text)

# EX3
# 서버가 느린 경우 타임아웃 줘서 출력값을 여유있게 받을 수 있음
r = s.get('https://github.com', timeout=5)

# 출력
print(r.text)

# POST
r = s.post('http://httpbin.org/post', data={'id':'test77', 'pw': '111'}, cookies=jar)

print(r.text)
print(r.headers)

# EX5
# 요청(POST)
payload1 = {'id': 'test17', 'pw': '111'}
# tuple 안에 tuple
payload2 = (('id','test88'), ('pw', '111'))

r = s.post('http://httpbin.org/post', data=payload2)
print(r.text)


# EX6
# PUT

r = s.put('http://httpbin.org/put', data=payload1)
print(r.text)

# EX7
# DELETE
r = s.delete('http://httpbin.org/delete', data={'id':1})

print(r.text)

r = s.delete('https://jsonplaceholder.typicode.com/posts/1', data={'id': 1})
print(r.ok)
print(r.text)
print(r.headers)

s.close()