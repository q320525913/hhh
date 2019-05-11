import requests


for i in range(1,11):
        url = 'http://python.jobbole.com/all-posts/page/' + str(i)
        response = requests.get(url)
        
        print('页面的状态吗为：',response.status_code)
        f = open('伯乐在线.txt','a',encoding='utf-8')   #创建 伯乐在线.txt的文本
        f.write(response.text)                          #在文本中写入数据
