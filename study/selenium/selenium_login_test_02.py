import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.ChromiumDriver(service=service)


def clipboard_input(self, user_xpath, user_input):
    pyperclip.copy(user_input)  # input을 클립보드로 복사
    # driver.find_element_by_xpath(user_xpath).click()  # element focus 설정
    driver.find_element(By.CSS_SELECTOR, user_xpath).click()  # element focus 설정
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()  # ctrl + v 전달


driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
# IDxPath = '//*[@id="id"]'
# PasswordxPath = '//*[@id="pw"]'
IDxPath = "#id"
PasswordxPath = "#pw"

# input으로 따로 입력을 받을 예정이므로 미리 적지 않아도 됩니다
ID = input("네이버 아이디: ")
Password = input("네이버 비밀번호: ")

clipboard_input(driver, IDxPath, ID)
clipboard_input(driver, PasswordxPath, Password)
# driver.find_element(By.CSS_SELECTOR, '//*[@value="로그인"]').click()
driver.find_element(By.CSS_SELECTOR, r'#log\.login').click()

# 새로운 기기 등록을 위한 창이 떴을 때, don't save를 클릭
driver.find_element(By.CSS_SELECTOR,r'#new\.dontsave').click()
