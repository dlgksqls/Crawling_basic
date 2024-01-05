# pip install requests

import requests

response = requests.get("https://www.naver.com")  # 네이버와 통신해라
html = response.text
print(html)
