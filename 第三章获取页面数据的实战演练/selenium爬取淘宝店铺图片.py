from selenium import webdriver
import requests
from lxml import etree
from hashlib import md5



def get_page_url(url):
    #设置不加载图片
    chrome_options = webdriver.ChromeOptions()
    #不加载图片，设置的参数很固定
    prefs = {"profile.managed_default_content_settings.images":2}   
    #将参数设置到chrome_opt里面
    chrome_options.add_experimental_option("prefs",prefs)
    #模拟浏览器的时候将chrome_opt添加进去
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    
    data = etree.HTML(driver.page_source)

    if url == 'https://shop148347845.taobao.com/?spm=2013.1.1000126.d21.7a461a3eHPsBHr':
        #获取店铺宝贝的链接
        store_url = data.xpath('//*[@class="item-name"]/@href')
        print('获取到的店铺宝贝链接为：'+store_url)
        driver.close()
        get_url(store_url)

    elif url.split('.')[-1] != 'jpg':
        #获取图片的链接
        jpg_url = data.xpath('//div[@id="description" ]//@src')
        driver.close()
        download_jpg(jpg_url)
def get_url(store_url):
        #合成url
        for store in store_url:
            if store != '' and store !=[]:
                url = 'https:' + store
                get_page_url(url)        

def download_jpg(jpg_url,list1=[]):
    #下载图片链接
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331'}

    
    for url in jpg_url:
        try:        #防止无效的图片链接出错
            if url not in list1 and url.split('.')[-1] != 'gif':
                list1.append(url)       #我爬到了一堆重复的链接，所以要去掉重复的链接
                response = requests.get(url,headers=headers)
                name = md5(url.encode('utf-8')).hexdigest()+'.jpg'  #获取摘要作为图片名字
                print('获取图片成功:',url,'现在已经获取了：',len(list1),'张图片')
                with open(name,'wb')as f:
                    f.write(response.content)
        except Exception as e:
            print('链接出错：',e)
if __name__ == '__main__':
    get_page_url('https://shop148347845.taobao.com/?spm=2013.1.1000126.d21.7a461a3eHPsBHr')
