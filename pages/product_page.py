import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By

# from selenium.common.exceptions import NoSuchElementException

from logger import logger

# from pages.cart_page import CartPage


class ProductPage:
    PRODUCT_NAME_H1_XPATH = "//h1[@class='prod-buy-header__title']"
    ADD_CART_BUTTON_XPATH = "//button[normalize-space(text())='장바구니 담기']"
    CART_QUICK_ACCESS_BUTTON_LINK_TEXT = "장바구니 바로가기"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.product_name = ""

    # 제품 상세 페이지로 이동
    def go_to_product_page(self, url):
        self.driver.get(url)

        ws(self.driver, 10).until(EC.url_contains("products"))
        assert "products" in self.driver.current_url

        self.product_name = self.driver.find_element(
            By.XPATH, self.PRODUCT_NAME_H1_XPATH
        ).text

        time.sleep(2)

        logger.info(f"✅ {self.product_name} 페이지로 이동 완료")

    # 장바구니 담기 클릭
    def click_add_cart(self):
        add_cart_button = self.driver.find_element(By.XPATH, self.ADD_CART_BUTTON_XPATH)
        add_cart_button.click()

        time.sleep(1)

        if not self.product_name:
            raise ValueError("❌ 상품명이 없습니다.")

        logger.info(f"🔄 {self.product_name} 추가")

        return self.product_name

    # 장바구니 바로가기 클릭
    # def click_cart_quick_access(self):
    #     try:
    #         go_to_cart_button = self.driver.find_element(
    #             By.LINK_TEXT, self.CART_QUICK_ACCESS_BUTTON_LINK_TEXT
    #         )
    #         go_to_cart_button.click()

    #         ws(self.driver, 10).until(EC.url_contains("products"))
    #         assert "products" in self.driver.current_url

    #         time.sleep(2)

    #         logger.info(f"✅ 장바구니 페이지로 이동 완료")
    #     except NoSuchElementException:
    #         logger.warning(f"❌ 장바구니 바로가기가 없습니다.")

    #         cart_page = CartPage(self.driver)
    #         cart_page.go_to_cart_page()

    # 옵션 선택
