import sys,os,time,pytest,allure
sys.path.append("..")
from Config.config import picture_path,account,password,js
from PageObject.room_page import Room_Page
from PageObject.login_page import LoginPage
from Libs.BasePage import BasePage
from selenium.webdriver.common.by import By
@allure.feature("添加房型")
class Test_room:
    def setup_class(self):
        LoginPage().get_url()
        LoginPage().login(account,password)

    @pytest.mark.add_room
    def test_add_room_success(self):
        Room_Page().implicity_waiting(2)
        Room_Page().add_rooms()
        Room_Page().sliding_page()

    @pytest.mark.repeat_add_room
    def test_repeat_add_room(self):
        Room_Page().implicity_waiting(2)
        Room_Page().add_rooms()
        Room_Page().sliding_page()
        BasePage().get_screen_shot(r"..\\Picture\\room_screenshot\\room_repeat.png")
        BasePage().wait_element((By.CSS_SELECTOR,".ant-message-notice-content >div >span:nth-child(2)"))
        room_repeat = BasePage().find_element(".ant-message-notice-content >div >span:nth-child(2)")
        assert room_repeat.text == "存在重名房型，请重新填写提交"

    @pytest.mark.quit
    def test_quit(self):
        BasePage().quit()

if __name__ == "__main__":
    pytest.main(["test_add_room.py","-s","-m=repeat_add_room","--alluredir","../Report/temp"])
    os.system("allure generate    ../Report/temp -o  ../Report/report --clean")


