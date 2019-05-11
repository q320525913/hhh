import requests
from random import choice

for i in range(20):
    ip =['112.85.168.5:9999','112.85.130.34:9999','113.121.22.35:9999','119.101.112.205:9999','112.85.129.129:9999','113.121.22.104:9999','223.241.118.157:8010','60.186.154.147:53281','119.101.112.191:9999','171.80.0.86:9999']
    random_ip = choice(ip)
    proxies = {'http':'http://'+ random_ip,'https':'https://' + random_ip}
    try:
        response=requests.get('http://python.jobbole.com/all-posts/page/'+str(i),proxies=proxies)
        if response.status_code == 200:
            print(response.status_code,'该ip可用',random_ip)
    except Exception:
        print('该ip：'+random_ip+'不可用')
