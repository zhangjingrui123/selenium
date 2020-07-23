import sys
import time
sys.path.append("..")
from Libs.BasePage import BasePage
from room_page import Get_login,Room_Page
from selenium.webdriver.common.by import By

'''价格方案页面封装
'''
class Get_Room:
    def get_room(self):                       #获取房型信息
        Get_login().set_up()
        Room_Page().implicity_waiting(2)
        Room_Page().add_rooms()
        Room_Page().sliding_page()      

class Room_Sale_Page(BasePage):
    def __init__(self):
        super(Room_Sale_Page,self).__init__()
        self.room_sale = (By.CSS_SELECTOR,".room-type_actionWrapper__34I4W >div:nth-child(2)")
        self.click_room_sale = (By.CSS_SELECTOR,".room-sale-type-form_addRoomSaleTypeButtonWrapper__3vaLQ >button")
        self.room_sale_name = (By.ID,"add-room-sale-type-form-modal_room_sale_name")
        self.room_sale_decription = (By.XPATH,"//input[@id='add-room-sale-type-form-modal_room_sale_description']")
        self.romm_sale_price = (By.XPATH,"//input[@id='add-room-sale-type-form-modal_room_sale_price']")
        self.romm_sale_amount = (By.XPATH,"//input[@id='add-room-sale-type-form-modal_room_sale_amount']")
        self.click_confim = (By.CSS_SELECTOR,".ant-modal-footer >div>button:nth-child(2)")
        self.used = (By.CSS_SELECTOR,".room-sale-type-form_tableActionWrapper__3z_E- >div:nth-child(1)")
    
    def add_room_sale(self):
        time.sleep(2)
        self.clicked(self.room_sale)
        self.clicked(self.click_room_sale)
        time.sleep(2)      
        self.sendkeys(self.room_sale_name,"大床房（含早）")
        self.sendkeys(self.room_sale_decription,"描述")
        self.sendkeys(self.romm_sale_price,"100")
        self.sendkeys(self.romm_sale_amount,"10")
        self.clicked(self.click_confim)
        time.sleep(2)
        self.clicked(self.used)

if __name__ == "__main__":
    Get_Room().get_room()
    Room_Sale_Page().add_room_sale()
    