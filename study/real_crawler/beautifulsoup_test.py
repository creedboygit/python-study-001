from bs4 import BeautifulSoup
import requests

response = requests.get("https://hosting.cafe24.com/?controller=new_product_page&page=images")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
word = soup.select_one('#skipNavigation')

print(word)
print()
print(word.text)
print()




