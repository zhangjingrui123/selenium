#域名：
url_path = "http://47.111.108.116:8082/"
#浏览器驱动对象：
chrome_driver = "D:\chromedriver\83\chromedriver.exe"
firefox_driver = "D:\chromedriver\80\chromedriver.exe"
#测试账号和密码：
account = "15266905059"
password = "123456"
#房型图片地址：
picture_path = r"D:\hotel_data\model4\1.jpg"
#点击房型图片，根据js获取元素属性：
js = "document.getElementsByClassName('ant-upload')[1].children[0].style.display='block';"
#上传身份证正面照，根据js修改元素属性：
js_front="document.getElementsByClassName('ant-upload')[1].children[0].style.display='block';"
front_picture = r"D:\hotel_data\ziliao\1.jpg"
#上传身份证反面照，根据js修改元素属性：
js_back = "document.getElementsByClassName('ant-upload')[3].children[0].style.display='block';"
back_picture = r"D:\hotel_data\ziliao\2.png"
#上传身份证半身照，根据js修改元素属性：
js_half = "document.getElementsByClassName('ant-upload')[5].children[0].style.display='block';"
half_picture = r"D:\hotel_data\ziliao\3.jpg"