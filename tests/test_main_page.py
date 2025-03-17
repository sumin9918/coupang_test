import time
from urllib import parse
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import MainPage

""" 
실행방법
- pytest tests/test_main_page.py
"""


@pytest.mark.usefixtures("driver")
class TestMainPage:
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            time.sleep(2)
        except NoSuchElementException as e:
            assert False

    # @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            # 로그인
            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            main_page.click_by_LINK_TEXT("로그인")

            assert "login" in driver.current_url
            driver.save_screenshot("메인페이지-로그인-성공.jpg")

            time.sleep(2)
            driver.back()

            # 회원가입
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2)

            main_page.click_by_LINK_TEXT("회원가입")

            assert "memberJoinFrm" in driver.current_url
            driver.save_screenshot("메인페이지-회원가입-성공.jpg")

            time.sleep(2)
            driver.back()

            # 장바구니
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url

            time.sleep(2)

            main_page.click_by_LINK_TEXT("장바구니")

            assert "cart" in driver.current_url
            driver.save_screenshot("메인페이지-장바구니-성공.jpg")

            time.sleep(2)
            driver.back()
        except NoSuchElementException as e:
            assert False

    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_search_items(self, driver: WebDriver):
        try:
            ITEMS_CLASS_NAME = "search-product"

            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            time.sleep(2)

            main_page.search_items("노트북")

            ws(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, ITEMS_CLASS_NAME))
            )

            items = driver.find_elements(By.CLASS_NAME, ITEMS_CLASS_NAME)
            item_name = parse.quote("노트북")

            assert len(items) > 0
            assert item_name in driver.current_url

            driver.save_screenshot("메인페이지-검색-성공.jpg")
        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-검색-실패-노서치.jpg")
            assert False

        except TimeoutError as e:
            driver.save_screenshot("메인페이지-검색-실패-타임아웃.jpg")
            assert False
