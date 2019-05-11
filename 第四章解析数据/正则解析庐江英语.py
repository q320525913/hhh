import re
import requests

headers = {'Cookie':'HJ_UID=c7ad95f2-7886-b96d-6648-f98722ab7b6e; _SREF_20=; _REF=; TRACKSITEMAP=20%2C; HJ_SID=6c649cad-6a2c-9438-af79-c1a6b358af8e; HJ_SSID_20=3f2b3274-4a4a-bf55-25c9-43a94f284d3c; HJ_CST=1; HJ_CSST_20=1; _SREG_20=direct|; _REG=direct|',
'Host':'jp.hjenglish.com',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.11096.400'}
response = requests.get('https://jp.hjenglish.com/zt/riyudc/',headers=headers)

title_re = re.compile('span.*?class="title".*?>(.*?)<',re.S)
content_re = re.compile('span.*?class="desc".*?>(.*?)<',re.S)

title = re.findall(title_re,response.text)
content = re.findall(content_re,response.text)
print(title,content)
