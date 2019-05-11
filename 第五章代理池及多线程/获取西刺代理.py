import requests
from lxml import etree
import redis

r = redis.Redis()
headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Mobile Safari/537.36'}

response = requests.get('https://www.xicidaili.com/nn/1',headers=headers)
data = etree.HTML(response.text)
ip = data.xpath('//tr[@class="odd"]/td[2]/text()')
port = data.xpath('//tr[@class="odd"]/td[3]/text()')

for i in range(len(ip)):
    #添加到redis的有序集合中,25是分数
    r.zadd('proxies',ip[i] + ':' + port[i],'25')
    



