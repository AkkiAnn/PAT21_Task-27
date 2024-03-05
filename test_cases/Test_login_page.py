import pytest
from openpyxl.styles import PatternFill
from datetime import datetime
from pages.Hme_page import Hme_page
from pages.Login_page import Login_page
from config.confe import BasePage
from utilityfile.ut_file import EXL

file = r"C:\Users\AkShay\PycharmProjectssaturday2724\pythonProject1\Task-27\Ta_27_EXL.xlsx"
sheetName = "Ta_27_EXL"


@pytest.mark.usefixtures("setup")
class Test_Login:
    def test_login(self):
        row = EXL.count_row(file, sheetName)
        for r in range(2,row+1):
            mail_ID = EXL.read_data(file, sheetName, r, 2)
            password = EXL.read_data(file, sheetName, r, 3)

            # obj of Login_Page
            login = Login_page(self.driver)
            HP= login.click_login(mail_ID, password)

            # Adding current Date to Excel
            run_date = datetime.now().strftime('%Y-%m-%d')
            EXL.write_data(file, sheetName, r, 4, run_date)

            # Adding current Time to Excel
            run_time = datetime.now().time().strftime('%H:%M:%S')
            EXL.write_data(file, sheetName, r, 5, run_time)

            try:
                assert HP.entering_the_home_page().is_displayed()
                EXL.write_data(file, sheetName, r, 6, 'AKSHAY M')
                EXL.write_data(file, sheetName, r, 8, 'TEST PASSED')

                # Filling Green_color to Excel cell
                EXL.fill_green_color(file, sheetName, r, 8)
                HP.logout()
            except:
                EXL.write_data(file, sheetName, r, 6, 'AKSHAY M')
                EXL.write_data(file, sheetName, r, 8, 'TEST FAILED')

                # Filling Red_color to Excel cell
                EXL.fill_red_color(file,sheetName,r, 8)
                HP.refresh()

# Run Tests
if __name__ == "__main__":
    pytest.main(["-v"])