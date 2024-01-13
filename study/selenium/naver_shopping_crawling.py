from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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





