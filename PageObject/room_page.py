'''
添加房型页面封装
'''
from selenium.webdriver.common.by import By
import os,sys,time
sys.path.append("..")
from Libs.BasePage import BasePage
from Config.config import picture_path,account,password,js


class Room_Page(BasePage):                          
    def __init__(self):
        super(Room_Page,self).__init__()                          #封装页面元素
        self.room_manage =(By.CSS_SELECTOR,".menu_wrapper__1zP1l >ul>li:nth-last-child(3)")
        self.add_room = (By.CSS_SELECTOR,".room-type_addRoomTypeButtonWrapper__-i6P2 >button")
        self.click_picture = (By.CSS_SELECTOR,".ant-upload > input")
        self.room_name = (By.XPATH,"//input[@id='room-type-set-form_room_name']")
        self.submit  = (By.CLASS_NAME,"room-type-set-form_actionWrapper__1n_R9")

    def add_rooms(self):
        time.sleep(2)
        self.clicked(self.room_manage)               #点击房型管理
        self.clicked(self.add_room)                  #点击添加房型
        self.execute_script(js)                      #点击上传图片
        self.sendkeys(self.click_picture,picture_path)#上传本地图片
        self.sendkeys(self.room_name,"大床房")       #输入房型名称

    def get_ele(self):
        return self.get_element(self.submit)

    def sliding_page(self):
        ele = Room_Page().get_ele()
        self.sliding_browser(ele)                  #滑动页面至元素可见
        self.clicked(self.submit)                  #  点击提交按钮
    
    def implicity_waiting(self,senonds):            #设置隐式等待
        self.implicitwait(senonds)

# if __name__ == "__main__":
#     Get_login().set_up()
#     Room_Page().implicity_waiting(2)
#     Room_Page().add_rooms()
#     Room_Page().sliding_page()        
    
    
