from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

import time


class MainPage:
    URL = "https://www.coupang.com"
    SEARCH_INPUT_ID = "headerSearchKeyword"

    # 객체를 인스턴스화
    # - 원하는 설정으로 셋업하는 함수
    # - driver : pytest의 fixture에서 제공하는 드라이브 (chrome)
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.URL)

        ws(self.driver, 10).until(EC.url_contains("coupang.com"))
        assert "coupang.com" in self.driver.current_url
        time.sleep(2)

    def search_items(self, item_name: str):
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)

    def click_by_LINK_TEXT(self, link_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, link_text)
        login_button.click()
