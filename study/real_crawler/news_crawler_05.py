import requests
from bs4 import BeautifulSoup
import pymsgbox as pm

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

# search_keyword = input("검색어를 입력해주세요 >>> ")
search_keyword = pm.prompt(text="검색어를 입력해주세요", title="검색어 입력", default="입력해주세요.")
last_page = int(pm.prompt(text="마지막 페이지를 입력해주세요"))

print("\nsearch_keyword: ", search_keyword, "\n")

# response = requests.get(
#     "https://search.naver.com/search.naver?where=news&sm=tab_jum&query="
#     + search_keyword,
#     headers=headers,
# )

pageNum = 1

# for i in range(1, 30, 10):
for i in range(1, last_page * 10, 10):
    print(f"{pageNum}페이지입니다. ==========================\n")

    response = requests.get(
        f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}&start={i}",
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

    pageNum += 1

    print()
