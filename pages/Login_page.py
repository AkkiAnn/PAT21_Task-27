from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.confe import BasePage
from pages.Hme_page import Hme_page

class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.email = (By.NAME,'username')
        self.password = (By.NAME, 'password')
        self.login_btn = (By.LINK_TEXT, ' Login ')

    # Login
    def click_login(self, email, code):
        self.BasePage.do_send_keys(self.email, email)
        self.BasePage.do_send_keys(self.password, code)
        self.BasePage.do_clicks(self.login_btn)
        return Hme_page(self.driver)