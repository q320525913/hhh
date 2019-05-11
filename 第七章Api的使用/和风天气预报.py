import requests


select_city = input('请输入天气情况')
url='https://free-api.heweather.net/s6/weather/now?key=4e8a588d1ea64d4bae729763c487bcfc&location={}'.format(select_city)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
response = requests.get(url,headers=headers)
print(response.text)
