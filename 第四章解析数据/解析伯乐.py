import requests
from lxml import etree

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 	Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2577.400'}

response = requests.get('http://python.jobbole.com/all-posts/',headers=headers)
data = etree.HTML(response.text)

title = data.xpath('//a[@class="archive-title"]/text()')
content = data.xpath('//span[@class="excerpt"]/p/text()')
for i in zip(title,content):
        print(str(i) + '\n\n')




