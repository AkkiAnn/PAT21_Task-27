from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.confe import BasePage as BP

class Hme_page:
    def __init__(self, driver):
        self.driver = driver

    account_name = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p")
    logout_text = (By.LINK_TEXT, 'Logout')

    def logout(self):
        self.driver.find_element(self.account_name)
        self.driver.find_element(self.logout_text)

    def refresh(self):
        self.driver.refresh()