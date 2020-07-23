'''
登录Case
'''
import sys,pytest,allure,os
sys.path.append("..")
from PageObject.login_page import LoginPage
from Libs.BasePage import BasePage
from Config.config import account,password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@allure.feature("登录")
class TestLogin:
    def setup_class(self):
        LoginPage().get_url()
    @pytest.mark.login_success
    def test_login_success(self):
        LoginPage().login("15266905059","123456")
        BasePage().get_screen_shot(r"..\\Picture\\login_screenshot\\login_success.png")
        BasePage().wait_element((By.CSS_SELECTOR,".ant-message-notice-content >div >span:nth-child(2)"))
        login_success = BasePage().find_element(".ant-message-notice-content >div >span:nth-child(2)")
        assert login_success.text == "登录成功"
        
    @pytest.mark.login_fail
    def test_login_fail(self):
        LoginPage().login("15266905059","12345678")
        BasePage().get_screen_shot(r"..\\Picture\\login_screenshot\\login_fail.png")
        BasePage().wait_element((By.CSS_SELECTOR,".ant-message-notice-content >div >span:nth-child(2)"))
        login_fail = BasePage().find_element(".ant-message-notice-content >div >span:nth-child(2)")
        assert login_fail.text == "密码错误"

    def test_quit(self):
        BasePage().quit()
if __name__ == "__main__":
    pytest.main(["test_login.py","-s","-m=login_success","--alluredir","../Report/temp"])
    os.system("allure generate    ../Report/temp -o  ../Report/report --clean")
    