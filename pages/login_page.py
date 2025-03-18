import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from logger import logger
from pages.main_page import MainPage
from login_info import LOGIN_INFO


class LoginPage:
    LOGIN_LINK_TEXT = "로그인"
    LOGOUT_LINK_TEXT = "로그아웃"
    ID_INPUT_ID = "login-email-input"
    PASSWORD_INPUT_ID = "login-password-input"
    LOGIN_BUTTON_XPATH = (
        "//button[normalize-space(text())='로그인']"  # text에 공백이 포함되어 있음
    )

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 로그인
    def login(self):
        try:
            # 메인 페이지 진입
            main_page = MainPage(self.driver)
            main_page.open()

            # 로그인 페이지 진입
            login_button = self.driver.find_element(By.LINK_TEXT, self.LOGIN_LINK_TEXT)
            login_button.click()

            assert "login" in self.driver.current_url

            time.sleep(2)

            # 로그인
            # 아이디 입력
            id_input = self.driver.find_element(By.ID, self.ID_INPUT_ID)
            id_input.send_keys(LOGIN_INFO["id"])

            time.sleep(30)

            # 비밀번호 입력
            password_input = self.driver.find_element(By.ID, self.PASSWORD_INPUT_ID)
            password_input.send_keys(LOGIN_INFO["password"])

            time.sleep(30)

            # 로그인 버튼 클릭
            login_button = self.driver.find_element(By.XPATH, self.LOGIN_BUTTON_XPATH)
            login_button.click()

            # 검증 : 로그아웃이 있으면 로그인 성공, 없으면 로그인 실패
            ws(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.LINK_TEXT, self.LOGOUT_LINK_TEXT)
                )
            )

            logger.info(f"✅ 로그인 완료")

        except NoSuchElementException as e:
            logger.warning(f"❌ 로그인 실패 - 오류 발생: {e}")
            assert False

        except TimeoutError as e:
            logger.warning(f"❌ 로그인 실패 - 오류 발생: {e}")
            assert False

    # 로그아웃
    def logout(self):
        try:
            # 메인 페이지 진입
            main_page = MainPage(self.driver)
            main_page.open()

            # 로그 아웃 버튼 클릭
            logout_button = ws(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.LINK_TEXT, self.LOGOUT_LINK_TEXT)
                )
            )
            logout_button.click()

            # 검증 : 로그인이 있으면 로그아웃 성공, 없으면 로그아웃 실패
            ws(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.LINK_TEXT, self.LOGIN_LINK_TEXT)
                )
            )

            logger.info(f"✅ 로그아웃 완료")

        except NoSuchElementException as e:
            logger.warning(f"❌ 로그아웃 실패 - 오류 발생: {e}")
            assert False

        except TimeoutError as e:
            logger.warning(f"❌ 로그아웃 실패 - 오류 발생: {e}")
            assert False
