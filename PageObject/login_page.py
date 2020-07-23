# from selenium import webdriver
'''
登录页面封装
'''
from selenium.webdriver.common.by import By
import sys
sys.path.append("..")
from Libs.BasePage import BasePage
from Config.config import account,password
class LoginPage(BasePage):                                         #定义login页面的元素及操作方法
    def __init__(self):                                            
        super(LoginPage,self).__init__()
        self.account  = (By.ID,"login_form_account")               #对象层：封装页面元素及操作对象
        self.password = (By.ID,"login_form_password")
        self.login_botton = (By.CLASS_NAME,"login_comfirmWrapper__37DjT")
        
    def get_url(self):                                             #操作层：分离具体的元素控件：用户名
        self.open_url()
        self.maximize_window()

    def login(self,account,password):                           
        self.sendkeys(self.account,account)    
        self.sendkeys(self.password,password)
        self.clicked(self.login_botton)

 
# if __name__ == "__main__":
#     LoginPage().get_url()
#     LoginPage().login(account,password)

        
