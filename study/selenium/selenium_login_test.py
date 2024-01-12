import time

import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.chrome import webdriver
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
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.ChromiumDriver(service=service)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)  # 웹페이지가 로딩될 때까지 5초 기다린다
driver.maximize_window()  # 화면 최대화

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
pyperclip.copy('1111')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy('1111')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, r"#log\.login")
login_btn.click()
