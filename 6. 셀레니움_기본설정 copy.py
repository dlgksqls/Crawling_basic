from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트

from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrom_options = Options()
chrom_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrom_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrom_options)

# 웹페이지 주소 이동
driver.get("https://www.naver.com")