import requests
from bs4 import BeautifulSoup

search_keyword = input("검색어를 입력해주세요 >>> ")
search_page = int(input("원하는 페이지까지 입력해주세요 >>> "))

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}


def make_search_url(search_keyword, start):

    search_url = (
        "https://search.naver.com/search.naver?where=news&query="
        + search_keyword
        + "&start="
        + start
    )

    return search_url


for i in range(search_page):

    start = str(i * 10 + 1)

    print("\nstart:", start)

    search_url = make_search_url(search_keyword, start)

    response = requests.get(search_url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    links = soup.select(".news_tit")

    # print(links)

    print("\n현재 페이지: ", i + 1)

    for link in links:
        title = link.text
        url = link.attrs["href"]

        print("제목:", title, "/", "링크:", url)



