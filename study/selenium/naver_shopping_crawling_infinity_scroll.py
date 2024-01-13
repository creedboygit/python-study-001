import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 자동 업데이트
service = Service(excutable_path=ChromeDriverManager().install())

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 제거
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# service = Service(excutable_path=ChromeDriverManager(driver_version="114.0.5735.90").install())
browser = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.ChromiumDriver(service=service)

browser.get("https://naver.com")
browser.implicitly_wait(10)

# 쇼핑 메뉴 클릭
# shopping_menu = browser.find_element(By.XPATH, r"//*[@id="shortcutArea"]/ul/li[4]/a")
shopping_menu = browser.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping")
shopping_menu.click()
time.sleep(1)

# 새 창을 바라보게 만들기
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# 화면 최대화
browser.maximize_window()

# 검색창 클릭
# search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search = browser.find_element(
    By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input'
)
search.click()

# 검색어 입력
# search.send_keys("아이폰")
search.send_keys("갤럭시 s10")
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다
    browser.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".product_item__MDtDF")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K").text

    try:
        price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    except (Exception,):
        price = "판매중단"

    link = item.find_element(
        By.CSS_SELECTOR, ".product_title__Mmw2K > a"
    ).get_attribute("href")

    print(f"{name} - {price} - {link}")
