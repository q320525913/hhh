import requests
import json

def getjson(loc,page_num=0):
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

text = getjson('广州市')


for i in text['results']:
    print(i['name'])
    print(i['address'])

#每个账号一天只有2000次的调用限额，如果进行了认证一天就会有10万次的调用限额

'''
参数      是否必须     默认值    示例         含义
Q            是          无     饭店、公园    检索关键字
Region       否          无   北京市、全国    检索区域（市级以上行政区域）
Scope        是          1       1、2         检索结果详细程度。若取值为1或空，
                                              返回基本信息：若取值为2，则返回检索
                                              POI详细信息
page_size    是          10      10-20        返回的数据，默认为10条记录，最大
                                              返回20条
page_num     否          0       0、1、2      分页页码，默认为0,0代表第一页，1代
                                              表第二页，以此类推。
Output       否          xml     xlm、json    输出格式为json或xml
AK           是          无      你的密匙     用户否访问密匙，必填项
'''
#文档地址：https://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi









