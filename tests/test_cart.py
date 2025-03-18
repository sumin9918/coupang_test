import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from logger import logger
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

"""
실행방법
- pytest tests/test_cart.py
"""

"""
장바구니 기능 테스트
- 웹 크롬으로 쿠팡 접속 후 상품을 장바구니에 추가한 후에 수량 변경, 삭제, 최대 수량 제한, 로그아웃 후 유지여부까지 전반적인 장바구니 기능이 정상 동작하는지 확인

steps
1. 상품 클릭 후 장바구니 담기 버튼 클릭
2. 장바구니 보기 클릭 후 장바구니 페이지 이동
3. 상품 수량 변경 클릭 후 변경된 수량과 결제 금액 반영 여부 확인
4. 일정 최대 수량 도달 후 후 클릭 불가 확인
5. 상품 삭제 버튼 클릭 후 목록에서 제거되는지 확인
6. 다시 상품 추가 후 로그아웃한 뒤 로그인하여 장바구니 유지 여부 확인


expectedResult
1. 상품 정상적으로 장바구니에 추가 확인
2. 수량 변경 시 수량과 결제 금액이 변경 되는 부분 확인
3. 일정 최대 수량 도달 후 수량 추가 불가능 (버튼 미작동)
4. 상품 삭제 시 삭제 및 목록에서 제거
5. 로그아웃 후 다시 로그인 해도 장바구니 상품 정상 확인
"""


@pytest.mark.usefixtures("driver")
class TestCart:
    # 네오북 2024 노트북 14.1 인텔 셀러론
    # URL = "https://www.coupang.com/vp/products/8082960833?itemId=22799436582&vendorItemId=89834367335&q=%EB%85%B8%ED%8A%B8%EB%B6%81&itemsCount=36&searchId=6da206395368174&rank=1&searchRank=1&isAddedCart="
    URL = "https://www.coupang.com/vp/products/7632841490?itemId=20281666746&vendorItemId=87349824874&sourceType=SDP_MID_CAROUSEL_2&clickEventId=0d909c60-03cf-11f0-9b49-31ef30edb928&templateId=3880&isAddedCart="

    # 1. 장바구니 추가 테스트
    # - page : 상품 상세 페이지
    # - action : 장바구니 담기 버튼 클릭
    # - expected result : 장바구니에 추가
    def test_add_product(self, driver: WebDriver):
        try:
            logger.info("🚀 장바구니 추가 테스트")

            # 로그인
            login_page = LoginPage(driver)
            login_page.login()

            # 상품 상세 페이지로 이동
            product_page = ProductPage(driver)
            product_page.go_to_product_page(self.URL)

            # 장바구니 담기 클릭
            # 장바구니에 담은 상품 이름 받기
            product_name = product_page.click_add_cart()

            # 장바구니 바로가기 클릭
            cart_page = CartPage(driver)
            cart_page.go_to_cart_page()

            # 장바구니에 있는 상품 이름 목록 받기
            product_names = product_page.get_product_names()

            # 방금 추가한 상품이 장바구니 목록에 있는지 확인
            assert product_name in product_names

            logger.info("✅ 상품 추가 완료")

        except NoSuchElementException as e:
            logger.warning(f"❌ 상품 추가 실패 - 오류 발생: {e}")
            assert False

        except ValueError as e:
            # product_name이 추가되지 않은 경우
            logger.warning(e)
            assert False
