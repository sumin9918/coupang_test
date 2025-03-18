import pytest
import time
from urllib import parse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from logger import logger
from pages.main_page import MainPage
from pages.login_page import LoginPage

""" 
실행방법
- pytest tests/test_search.py
"""

"""
상품 검색 기능 테스트
- 웹 크롬으로 접속 후 검색 기능 정상 작동 여부 확인

steps
1. 쿠팡 로그인 전 : 검색 기능에 노트북 작성 -> 검색 버튼
2. 쿠팡 로그인 후 : 검색 기능에 노트북 작성 -> 검색 버튼

expectedResult
1. 로그인 전/후 검색 기능 이상 없음
2. 검색 내용과 관련된 내용 순차적으로 상품 정렬
"""

# @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")


@pytest.mark.usefixtures("driver")
class TestSearch:
    SEARCH_TEXT = "노트북"
    SEARCH_ITEM_CLASS_NAME = "search-product"

    # 1. 쿠팡 로그인 하지 않은 상태에서 검색창에 노트북 검색
    def test_search_without_login(self, driver: WebDriver):
        try:
            logger.info("🚀 비로그인 검색 테스트")

            # 쿠팡 메인 페이지 진입
            main_page = MainPage(driver)
            main_page.open()

            # 검색
            main_page.search_items(self.SEARCH_TEXT)

            # 검색한 내용을 확인
            items = ws(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, self.SEARCH_ITEM_CLASS_NAME)
                )
            )

            time.sleep(2)

            assert len(items) > 0
            assert parse.quote("노트북") in driver.current_url

            logger.info(f"✅ {self.SEARCH_TEXT} 검색 성공 - {len(items)}개 항목 찾음")

        except NoSuchElementException as e:
            logger.warning(f"❌ 검색 실패 - 오류 발생: {e}")
            assert False

    # 2. 쿠팡 로그인 한 상태에서 검색창에 노트북 검색
    def test_search_with_login(self, driver: WebDriver):
        try:
            logger.info("🚀 로그인 검색 테스트")

            # 로그인
            login_page = LoginPage(driver)
            login_page.login()

            # 검색
            main_page = MainPage(driver)
            main_page.search_items(self.SEARCH_TEXT)

            # 검색한 내용을 확인
            items = ws(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, self.SEARCH_ITEM_CLASS_NAME)
                )
            )

            time.sleep(2)

            assert len(items) > 0
            assert parse.quote("노트북") in driver.current_url

            logger.info(f"✅ {self.SEARCH_TEXT} 검색 성공 - {len(items)}개 항목 찾음")

        except NoSuchElementException as e:
            logger.warning(f"❌ 검색 실패 - 오류 발생: {e}")
            assert False
