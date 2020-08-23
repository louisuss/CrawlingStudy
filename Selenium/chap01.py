# Selenium
# 후처리 되는 렌더링을 통해서 정보를 표시해주는 서버쪽 프로그래밍이 되어있는
# 사이트들은 requests 모듈이나 urllib로 조회 했을 때 reponse 데이터가 없음
# 실질적으로 보안이 들어가 있는 사이트 접근할 때 진짜 브라우저 드라이버를 통해
# 접근해야 브라우저인지 알고 정상적으로 사용자에게 주는 정보를 response

# Selenium 실습 (1) - 설정 및 기본 테스트


from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
# 전체 경로 넣어줘야됨
browser = webdriver.Chrome(
    '/Users/louis/Python/AdvancedPython/Crawling/Selenium/chromedriver')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 속성 확인
# print(dir(browser))

# 브라우저 사이즈 지정
# maximize_window(), minimize_window()
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get('https://www.daum.net')

# 페이지 내용 출력
print('Page Contents: {}'.format(browser.page_source))
print()

# 세션 값 출력
print('Session ID: {}'.format(browser.session_id))

# 타이틀 출력
print('Title: {}'.format(browser.title))

# 현재 URL 출력
print('URL: {}'.format(browser.current_url))

# 현재 쿠키 정보 출력
print('Cookies: {}'.format(browser.get_cookies()))

# 검색창 input 선택
# 핵심
element = browser.find_element_by_css_selector(
    'div.inner_search > input.tf_keyword')

# 검색어 입력
element.send_keys('방탄소년단')

# 검색(Form Submit)
element.submit()

# 스크린 샷 저장1
browser.save_screenshot("/Users/louis/website_photo1.png")

# 스크린 샷 저장2
browser.get_screenshot_as_file("/Users/louis/website_photo2.png")

# 브라우저 종료
browser.quit()
