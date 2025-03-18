import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from logger import logger


class CartPage:
    GO_TO_CART_BUTTON_LINK_TEXT = "장바구니"
    PRODUCT_NAMES_CLASS_NAME = "product-name"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 장바구니 페이지로 이동
    def go_to_cart_page(self):
        go_to_cart_button = self.driver.find_element(
            By.LINK_TEXT, self.GO_TO_CART_BUTTON_LINK_TEXT
        )
        go_to_cart_button.click()

        ws(self.driver, 10).until(EC.url_contains("products"))
        assert "products" in self.driver.current_url

        time.sleep(2)

        logger.info(f"✅ 장바구니 페이지로 이동 완료")

    # 장바구니 상품 이름 목록 반환
    def get_product_names(self):
        product_names = [
            e.text
            for e in self.driver.find_elements(
                By.CLASS_NAME, self.PRODUCT_NAMES_CLASS_NAME
            )
        ]

        return product_names
