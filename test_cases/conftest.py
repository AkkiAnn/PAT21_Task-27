import pytest
from selenium import webdriver

driver = None
driver_path = (r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")
orangeHRM_url = ("https://opensource-demo.orangehrmlive.com/")

@pytest.fixture(scope="class")
def setup(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(orangeHRM_url)
    request.cls.driver = orangeHRM_url

    yield driver
    # Teardown Chrome driver
    driver.quit()
