import sys,os,time
sys.path.append("..")
from Config.config import picture_path,account,password,js
from PageObject.room_page import Get_login,Room_Page
from PageObject.login_page import LoginPage
class TEST_Add_room:
    def add_room(self):
        Get_login.set_up()
        time.sleep(2)
        add_room_ob = Room_Page()
        add_room_ob.room_click()
        add_room_ob.up_picture()
        time.sleep(3)
        add_room_ob.room_send_keys()
        add_room_ob.sliding_page()

if __name__ == "__main__":
    TEST_Add_room().add_room()
    
