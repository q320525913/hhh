from selenium import webdriver
import time

driver = webdriver.Chrome()                     #使用谷歌浏览器
driver.get('http://quotes.toscrape.com/js/')    #打开这个url地址
driver.execute_script("window.scrollBy(0,3000)")#向下滚动3000个像素
time.sleep(1)
print('第一页url：' + driver.current_url)
#如果找不到元素就会报堆栈错误
driver.find_element_by_xpath('html/body//li[@class="next"]/a').click()    
print('第二页url：' + driver.current_url)












