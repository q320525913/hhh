import requests
import json

def getjson(name):

    url = 'http://api.map.baidu.com/geocoder/v2/?'
    
    pa = {'ak':'suGxfVwjkVFWW62jBSR8iiwNcOZVyFaW',
          'output':'json',
          'address':name,
          'callback':'showLocation',
          'ret_coordtype':'bd09ll'}
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    r = requests.get(url,params=pa,headers=headers)
    return r.text
   

test = getjson('广州动物园')
lng = test.split('"lng":')[1].split(',')[0]
lat = test.split('"lat":')[1].split('}')[0]
location = lng+','+lat
print(location)

#每个账号一天只有2000次的调用限额，如果进行了认证一天就会有10万次的调用限额

'''
参数      是否必须      类型      举例    

ak	     是         strint           
address      是         string    北京市海淀区上地十街10号
含义                 1、标准的结构化地址信息，如北京市海淀区上地十街十号
                     2、支持“*路与*路交叉口”描述方式，如北一环路和阜阳路的交叉路口
output	     否         string      表示输出类型，可设置为xml或json。
city         否         string    北京市
含义                 地址所在的城市名。用于指定上述地址所在的城市，当
                     多个城市都有上述地址时，该参数起到过滤作用，但不限制坐标召回城市。
ret_coordtype否         string    gcj02ll（国测局坐标）、bd09mc（百度墨卡托坐标）
含义                  添加后返回国测局经纬度坐标或百度米制坐标
sn           否         string           含义  若用户所用ak的校验方式为sn校验时该参数必须 
callback     否         string    callback=showLocation(JavaScript函数名)
含义                  将json格式的返回值通过callback函数返回以实现jsonp功能
'''
#文档地址：https://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding

