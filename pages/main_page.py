import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

from logger import logger


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

        logger.info("✅ 메인 페이지 오픈")

        time.sleep(2)

    def search_items(self, search_text: str):
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        search_input_box.send_keys(search_text)
        search_input_box.send_keys(Keys.ENTER)

        logger.info(f"🔍 {search_text} 검색 실행")

    def click_by_LINK_TEXT(self, link_text: str):
        link_button = self.driver.find_element(By.LINK_TEXT, link_text)
        link_button.click()
