# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# daum에 대화 시도
response = requests.get("https://www.daum.net/")

# daum 에서 html을 줌
html = response.text

# html 번역선생님으로 수프 만듬 class = . id = #
soup = BeautifulSoup(html, "html.parser")
# soup.select # 여러개 태그 선택
word = soup.select_one(".cMain")  # 딱 한개 태그 선택 ,, 아이디 선택시 앞에 # 붙이기
print(word)
