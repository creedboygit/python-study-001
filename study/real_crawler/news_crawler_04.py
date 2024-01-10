import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

search_keyword = input("검색어를 입력해주세요 >>> ")

response = requests.get(
    "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
    + search_keyword,
    headers=headers,
)
html = response.text

soup = BeautifulSoup(html, "html.parser")
# print(soup)
links = soup.select(".news_tit")

# print(links)

for link in links:
    title = link.text
    url = link.attrs["href"]

    print("제목:", title, "/", "링크:", url)
