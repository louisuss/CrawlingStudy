# BeautifulSoup 사용 스크래핑(1)

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dobi's Story</title>
    </head>
    <body>
        <h1>H1</h1>
        <h2>H2</h2>
        <p class="title"><b>The Dobi's story</b></p>
        <p class="story">Once upon a time 
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lasie" class="sister" id="link2">Lasie</a>
            <a data-io="link3" href="http://example.com/little" class="brother" id="link3">Little</a>
        </p>
        <p class="story">
            story...
        </p>
    </body>
</html>
"""

# Ex1
# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))
print('prettify', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1: ', h1)

# p 태그 접근
# p 태그가 3개 있지만 첫번째 태그만 가져옴
p1 = soup.html.body.p
print('p1: ', p1)

# 공백 호출(커서가 이전 p태그 끝에 위치)
# print(p1.next_sibling)

# # 다음 다음 p 태그
p2 = p1.next_sibling.next_sibling
print('p2: ', p2)

# 텍스트 출력
print('h1 >>', h1.string)

# 텍스트 출력2
print('p1 >>', p1.string)

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
# 사용 잘 안함
# print(p2.next_element)

# 반복 출력 확인
# for v in p2.next_element:
#     print(v)

# find, find_all
# bs4 초기화
soup2 = BeautifulSoup(html, 'html.parser')
link1 = soup.find_all('a', limit=2)
# print(type(link1))
print('link1 >>> ', link1)
print()

# id='link2', string='title', string=["Elsie"]
link2 = soup.find_all('a', class_='sister')
print(link2)
print()

# 중요
# 태그 이외의 속성 값 또는 태그 하위에 있는 string 문자열로도 조건 만들어 가져올 수 있음
link2 = soup.find_all('a', string=["Elsie", "Little"])
print(link2)

for t in link2:
    print(t)


# 처음 발견한 a 태그 선택
link3 = soup.find('a')
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건(중요)
link4 = soup.find('a', {"class": 'brother', "data-io": "link3"})
print(link4)
print(link4.string)
print(link4.text)

# css 선택자: selct_one, select
# 태그로 접근: find, find_all
# select, select_one
# 태그 + 클래스 + 자식선택자
# . 클래스 가져올 때 사용
# p->title->자식태그하위 b태그 가져옴
link5 = soup.select_one('p.title > b')
print(link5)
print(link5.string)
print(link5.text)

# # -> id값 가져올 때 사용
link6 = soup.select_one("a#link1")
print(link6)
print(link6.string)
print(link6.text)

# [] -> 속성값 접근 가능
link7 = soup.select_one("a[data-io='link3']")
print(link7)
print(link7.string)
print(link7.text)

# 선택자에 맞는 전체 선택
link8 = soup.select('p.story > a')
# list 형태임
print(link8)
for v in link8:
    print(v.string)

# p태크 클래스 이름 story 하위 a태그들 중에서 두번째인 것 가져오기
link9 = soup.select('p.story > a:nth-of-type(2)')
print(link9)

link10 = soup.select("p.story")
print(link10)
print()

for t in link10:
    temp = t.find_all('a')
    if temp:
        for v in temp:
            print('>>>>', v)
            print('>>>>', v.string)
    else:
        print('-----', t)
        print('-----', t.string)