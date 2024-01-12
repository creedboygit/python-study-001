import openpyxl
import requests
from bs4 import BeautifulSoup

fpath = r"D:\940 python_study\200 study\210 basic\pythonProject\study\stock_crawler\files\data.xlsx"
wb = openpyxl.load_workbook(fpath)
ws = wb.active

# 종목 코드 리스트
codes = ["005930", "000660", "035720"]

row_num = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    price = soup.select_one("#_nowVal").text
    price = price.replace(",", "")
    print(price)

    ws[f"B{row_num}"] = int(price)

    row_num += 1

wb.save(fpath)
