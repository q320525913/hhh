import requests
import json


def park(loc,page_num=0):
    url = 'http://api.map.baidu.com/place/v2/search?'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    pa = {'q':'公园',
          'region': loc,
          'scope':'2',
          'page_size':'20',
          'output':'json',
          'ak':'1eHRqys109MfLs4P3oA22qKXieLdKfh3',}
    r = requests.get(url,params=pa,headers=headers)
    decodejson = json.loads(r.text)
    return decodejson

def Coordinates(name):

    url = 'http://api.map.baidu.com/geocoder/v2/?'
    
    pa = {'ak':'1eHRqys109MfLs4P3oA22qKXieLdKfh3',
          'output':'json',
          'address':name,
          'callback':'showLocation',
          'ret_coordtype':'wgs84ll'}
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    r = requests.get(url,params=pa,headers=headers)
    return r.text
def get_jpg(location,name):
    url = 'http://api.map.baidu.com/panorama/v2?'
    pa = {'ak':'1eHRqys109MfLs4P3oA22qKXieLdKfh3',
          'width':'512',
          'height':'256',
          'location':location,
          'fov':'180'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    r = requests.get(url,params=pa,headers=headers)
    with open(name+'.jpg','wb')as f:
        f.write(r.content)


text = park('广州市')
for i in text['results']:
    name = i['name']
    address = i['address']
    test = Coordinates(address)
    lng = test.split('"lng":')[1].split(',')[0]
    lat = test.split('"lat":')[1].split('}')[0]
    location = lng+','+lat
    print(location)
    get_jpg(location,name)   

