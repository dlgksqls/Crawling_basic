# pip install pyautogui

import requests
from bs4 import BeautifulSoup
import pyautogui

count = 0
keyword = pyautogui.prompt("검색어를 입력하세요.")
lastpage = pyautogui.prompt("마지막 페이지번호를 입력해 주세요")
# response = requests.get(
#     "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword
# )

for i in range(1, int(lastpage) * 10, 10):
    count += 1
    print(" ")
    print(
        f"############################################{count} 페이지#######################################"
    )
    print(" ")
    response = requests.get(
        f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}"  # start를 넣어서 페이지 조정
    )
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".news_tit")
    for link in links:
        title = link.text  # 태그 안에 텍스트요소를 가져온다
        url = link.attrs["href"]  # herf의 속성값을 가져온다
        print(title, url)
