# # 아래 코드 driver 안되는데 찾아보기
# # from selenium import webdriver

# # 브라우저 생성
# browser = webdriver.Chrome(r'C:\chromedriver-win64\chromedriver.exe')
# # 웹 사이트 열기
# browser.get('https://www.naver.com')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우저 꺼짐 방지
chrom_options = Options()
chrom_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrom_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrom_options)

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌
browser.maximize_window()
# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR,'#shortcutArea > ul > li:nth-child(4) > a > span.service_icon.type_shopping').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, '._searchInput_search_text_3CUDs')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)
