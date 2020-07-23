'''
封装个人认证页面
'''

import sys
import time
sys.path.append("..")
from Libs.BasePage import BasePage
from login_page import LoginPage
from selenium.webdriver.common.by import By
from Config.config import account,password,js_front,front_picture,js_back,back_picture,js_half,half_picture
class Get_login:
    def set_up(self):
        LoginPage().get_url()
        LoginPage().login(account,password)

class Audit_Page(BasePage):
    def __init__(self):
        super(Audit_Page,self).__init__()
        self.welcome = (By.CSS_SELECTOR,".welcome_comfirmWrapper__qB0oA >button")
        self.agree = (By.CSS_SELECTOR,".ant-modal-footer >div > button:nth-child(2)")
        self.name = (By.ID,"user-audit-form_personAuditName")
        self.id_card = (By.ID,"user-audit-form_identityCardNumber")
        self.select_front = (By.XPATH,"//*[@id='user-audit-form']/div/div[3]/div[1]/div[2]/div/div/span/div/span/input")
        self.select_back = (By.XPATH,"//*[@id='user-audit-form']/div/div[3]/div[2]/div/div/div/span/div/span/input")
        self.select_half = (By.XPATH,"//*[@id='user-audit-form']/div/div[4]/div/div/div/div/span/div/span/input")
        self.next_step = (By.CSS_SELECTOR,".user-audit-form_actionWrapper__Wb0i7 >button") 
    def person_verified(self):
        self.clicked(self.welcome)
        time.sleep(1)
        self.clicked(self.agree)
        time.sleep(2)
        self.sendkeys(self.name,"张三")
        self.sendkeys(self.id_card,"140825199604200015")
        time.sleep(1)
        self.execute_script(js_front)
        self.sendkeys(self.select_front,front_picture)
        time.sleep(2)
        self.execute_script(js_back)
        self.sendkeys(self.select_back,back_picture)
        time.sleep(2)
        self.execute_script(js_half)
        self.sendkeys(self.select_half,half_picture)
    
    def get_ele(self):
        return  self.get_element(self.next_step)

    def next(self):
        ele = Audit_Page().get_ele()
        self.sliding_browser(ele) 
        self.clicked(self.next_step)

    def verified_waiting(self,seconds):
        self.implicitwait(seconds)
if __name__ == "__main__":
    Get_login().set_up()
    Audit_Page().verified_waiting(2)
    Audit_Page().person_verified()
    Audit_Page().next()

