import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from lxml import etree

EMAIL = '论坛帐号'
PASSWORD = '论坛密码'

CHAOJIYING_USERNAME = '超级鹰帐号'
CHAOJIYING_PASSWORD = '超级鹰密码'
CHAOJIYING_SOFT_ID = 898391

class CrackTouClick():
    def __init__(self):
        self.url = 'https://passport.cnblogs.com/user/signin'
        self.option = ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = Chrome(options=self.option)
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
    
 
    def open(self):
        """
        打开网页输入用户名密码
        以及点击验证按钮的操作
        """
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'input1'))).send_keys(self.email)
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'input2'))).send_keys(self.password)
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button'))).click()
        button2 = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_btn'))).click()

    
        try:
            #slider判断是滑块验证码还是字体验证码
            slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))                 
            CHAOJIYING_KIND = 9202                       #验证码类型
            print('这是滑块验证码')
            image = self.get_touclick_image()            #获取图片
                       # 识别验证码
            result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
            print('验证码位置',result['pic_str'])
            print(result)
            locations = self.get_points(result)
            self.touch_click_words(locations)
            print('正在检测错误,此处延迟3秒,以便等待页面加载')
            time.sleep(3)
            self.img_error(result)
        except Exception as e:
            print('这是字体验证码',e)
            CHAOJIYING_KIND = 9103                      #验证码类型
            # 获取验证码图片
            image = self.get_touclick_image()           #获取图片
            bytes_array = BytesIO()
            image.save(bytes_array, format='PNG')       ##保存一张图片来参照
            
            # 识别验证码
            result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
            print(result)

            locations = self.get_points(result)
            self.touch_click_words2(locations)
            print('正在检测错误,此处延迟3秒,以便等待页面加载')
            time.sleep(3)
            self.img_error(result)
    def touch_click_verify(self):
        """
        获取滑块按钮
        :return: None
        """
        
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def get_touclick_element(self):
        """
        获取验证图片对象
        :return: 图片对象
        """
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_slice')))
        return element
    
    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)
    
    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot
    
    def get_touclick_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha
    
    def get_points(self, captcha_result):
        """
        解析识别结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        """
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        """
        点击滑块验证图片
        :param locations: 点击位置
        :return: None
        """
        for location in locations:
            print(location)
            ActionChains(self.browser).drag_and_drop_by_offset(self.touch_click_verify(), location[0],
                                                                   location[1]).perform()
            time.sleep(1)


    def touch_click_words2(self, locations):
        """
        点击字体验证图片
        :param locations: 点击位置
        :return: None
        """
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_touclick_element(), location[0],
                                                                   location[1]).click().perform()
            time.sleep(1)


    def img_error(self,result):
        #检测验证码有没有出错,这步老是报出栈错误
        #无奈之下只能采取解析式来判断登录前后页面的数据了
        #不得不吐槽的是,这里的滑块验证码坐标识别率低到了令人发指的地步
        test = etree.HTML(self.browser.page_source)
        title = test.xpath('//*[@id="app_ing"]/text()')
        print('爬取登陆前后的数据变化',title)
        if title == []:
            img_id = result['pic_id'] 
            self.chaojiying.report_error(img_id)
            print('登录失败,已发送错误验证码')
            self.open()
            
        else:
            print('登录成功')    

        
if __name__ == '__main__':
    #值得注意的是,千万不要在页面开启审查元素,不然页面结构会有所改变
    #这样的页面结构是完全不可能识别验证码成功的
    crack = CrackTouClick()
    crack.open()

