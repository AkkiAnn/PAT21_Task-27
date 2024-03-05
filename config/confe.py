from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # send_keys block
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # click block
    def click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()