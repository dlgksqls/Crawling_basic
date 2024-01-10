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
import csv

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
browser.get("https://www.naver.com/")
browser.implicitly_wait(10)  # 로딩이 끝날 때까지 10초까지는 기다려줌

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping").click()
time.sleep(2)

# 새창을 바라보게 만들기
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# 화면 최대화
browser.maximize_window()

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys("아이폰13")
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤

while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성
f = open(
    r"C:\Users\horai\Desktop\Crawling_basic\Crawling_basic\3. 네이버_쇼핑_크롤링\data.csv",
    "w",
    encoding="CP949",
    newline="",
)
csvWriter = csv.writer(f)

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".product_item__MDtDF")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K").text
    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    except:
        price = "판매중단"
    link = item.find_element(
        By.CSS_SELECTOR, ".product_title__Mmw2K > a"
    ).get_attribute("href")

    print(name, price, link)
    csvWriter.writerow([name, price, link])

f.close()

# try:
#     price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
# except:
#     price = "판매중단"
