from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = '8934c63a'
desired_caps['appPackage'] = 'com.sankuai.meituan.takeoutnew'
desired_caps['appActivity'] = '.ui.page.boot.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)
time.sleep(7)
driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/layout_search_box_normal"]').click()
driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/search_action_bar_container"]').send_keys('hanbao')
driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/search_tv"]').click()

x = driver.get_window_size()['width']  
y = driver.get_window_size()['height']

for i in range(11):
    data = driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/textview_poi_name"]').text
    driver.swipe(0, 3/7*y, 0,1/7*y, 2000)
    print(data)
    
    


