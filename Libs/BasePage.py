'''基础对象库层：封装所有页面公共的定位元素的方法,基类，所有的页面都该继承该类
操作页面层：  封装页面的元素对象和操作方法
测试层：      对业务逻辑进行封装，数据驱动
'''
import sys
sys.path.append("..")
from  Config.config import url_path,chrome_driver,firefox_driver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import win32com.client


class Driver:                                                   
    _browser = None                                              #获取浏览器驱动对象，默认为Chrome浏览器
    @classmethod
    def get_driver(cls,browser_name = "chrome"):
        if cls._browser is None:
            if browser_name == "chrome":
                cls._browser = webdriver.Chrome(chrome_driver)
            elif browser_name == "firefox":
                cls._browser = webdriver.Firefox(firefox_driver)
            else:
                raise NameError("找不到任何浏览器，请重新设置")
        return cls._browser

class BasePage:                                            
    def __init__(self):
        self.driver = Driver.get_driver()                          #用类调用类方法，获取到driver对象
            
    def open_url(self,url=url_path):                               #获取浏览器url地址
        self.driver.get(url)

    def get_element(self,locator):                                 #设置定位元素方法
        return self.driver.find_element(*locator)

    def get_elements(self,locator):
        return self.driver.find_elements(*locator)

    def clicked(self,locator):                                       #点击 
        self.get_element(locator).click()

    def sendkeys(self,locator,content):                            #输入内容的方法
        self.get_element(locator).send_keys(content)
       
    def maximize_window(self):                                   
        self.driver.maximize_window()                               #浏览器最大化
        # self.driver.refresh()                                     #浏览器刷新
        # self.driver.forward()
        # self.driver.back()
        # self.driver.title
        # self.driver.curent_url
    def wait_element(self,locator,timeouts =3,polltime=0.5):       #定位元素方法
        try:
            element = WebDriverWait(self.driver,timeouts,polltime).until(ec.presence_of_element_located(locator))
            return element
        except:
            print("%s页面元素未找到 %s" % (self.locator))

    def get_attribute(self,locator,name):
        return self.get_element(locator).get_attribute(name)
        
    def clear(self,locator):
        self.get_element(locator).clear()                                   #清除指定元素输入框中的数据
    
    def implicitwait(self,seconds):                                #设置隐式等待
        self.driver.implicitly_wait(seconds)

    def get_screen_shot(self,file_path):                             #截屏处理
        return self.driver.get_screenshot_as_file(file_path)       
    
    def switch_to_frame(self,ele):                                   #切换到iframe内嵌页面
        self.driver.switch_to_frame(ele)                             

    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()                      #从frame页面切换回原页面

    def upload_file(self,file_path):                                  #上传图片           
        sh = win32com.client.Dispatch("WScript.shell")
        sh.SendKeys(file_path + "{ENTER}" + "\n")
    
    def select(self,locator,value,index=0):  
        ele = self.get_element(locator)                            #下拉选择元素
        select_index = Select(ele).select_by_index(index)          #根据下标选择元素
        select_value = Select(ele).select_by_value(value)          #根据属性值选择元素
        return select_index,select_value

    def action_chains(self,ele):                                    #鼠标悬停到指定界面
        ActionChains(self.driver).move_to_element(ele).perform()


    def sliding_browser(self,ele):                                   #滑动浏览器页面至元素可见
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)

    def execute_script(self,js):
        self.driver.execute_script(js)
    
    def find_element(self,locator):
        return self.driver.find_element_by_css_selector(locator)

    def quit(self):                                                       #退出浏览器
        self.driver.quit()  


if __name__ == "__main__":                                                 #测试调用
    BasePage().open_url()    
    BasePage().maximize_window()                                          #获取url地址
    BasePage().sendkeys((By.ID,"login_form_account"),"15266905059")
    BasePage().sendkeys((By.ID,"login_form_password"),"123456")
    BasePage().clicked((By.CLASS_NAME,"login_comfirmWrapper__37DjT"))
    # BasePage().quit()