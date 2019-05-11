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
time.sleep(5)
driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/layout_search_box_normal"]').click()
driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/search_action_bar_container"]').send_keys('hanbao')
driver.find_element_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/search_tv"]').click()
data = driver.find_elements_by_xpath('//*[@resource-id="com.sankuai.meituan.takeoutnew:id/textview_poi_name"]')
for i in data:
    print(i.text)
