import requests
from lxml import etree
from redis import Redis

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.11096.400'}

number  = [0,1,2,3,4,5,6,7,8,9]
r = Redis()
class agent():
    def __init__(self):
        self.headers = headers
        self.r = r
        self.number = number
    def agent_xici(self):       #获取西刺代理
        response = requests.get('https://www.xicidaili.com/nn/1',headers=self.headers)
        data = etree.HTML(response.text)
        ip = data.xpath('//tr[@class="odd"]/td[2]/text()')
        port = data.xpath('//tr[@class="odd"]/td[3]/text()')

        for i in range(len(ip)):
            #print(ip[i] + ':' + port[i])
            self.r.zadd('proxies',ip[i] + ':' + port[i],'25')
        print('代理1号爬取完成')
    def agent_31f(self):        #获取31f代理
        response = requests.get('http://31f.cn/',headers=self.headers)
        data = etree.HTML(response.text)
        ip = data.xpath('//*[@class="table table-striped"]//td[2]/text()')
        port = data.xpath('//*[@class="table table-striped"]//td[3]/text()')

        for i in range(len(ip)):
            #print(ip[i] + ':' + port[i])
            self.r.zadd('proxies',ip[i] + ':' + port[i],'25')
        print('代理2号爬取完成')
    def agent_66ip(self):       #获取66ip代理
        #这个网站需要cookie还     要解码
        headers66 = {'Cookie':'__jsluid=e06ebc02bdc84f9174a9bfdf570f5dfe; __jsl_clearance=1557209135.06|0|7BXM5eo%2B3mZ%2FYyBvDmTponPu8WQ%3D',
                    'Host':'www.66ip.cn',
                    'Referer':'http://www.66ip.cn/index.html',
                    'Upgrade-Insecure-Requests':'1',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.11096.400'}

        response = requests.get('http://www.66ip.cn/index.html',headers=headers66)
        data = etree.HTML(response.content.decode('gb2312'))
        ip = data.xpath('//*[@align="center"]//td[1]/text()')
        port = data.xpath('//*[@align="center"]//td[2]/text()')

        for i in range(len(ip)):
            if ip[i] != 'ip': 
                #print(ip[i] + ':' + port[i])
                self.r.zadd('proxies',ip[i] + ':' + port[i],'25')
        print('代理3号爬取完成')
    def agent_89ip(self):       #获取89ip代理
        response = requests.get('http://www.89ip.cn/',headers=headers)
        data = etree.HTML(response.text)
        ip = data.xpath('//*[@class="layui-table"]//td[1]/text()')
        port = data.xpath('//*[@class="layui-table"]//td[2]/text()')

        for i in range(len(ip)):#得到好多换行符和制表符，所以要用strip去除
            #print(ip[i].strip() + ':' + port[i].strip())
            self.r.zadd('proxies',ip[i].strip() + ':' + port[i].strip(),'25')
        print('代理4号爬取完成')
    def agent_kuaidaili(self):  #获取kuaidaili代理
        response = requests.get('https://www.kuaidaili.com/free/',headers=headers)
        data = etree.HTML(response.text)
        ip = data.xpath('//*[@class="table table-bordered table-striped"]//td[1]/text()')
        port = data.xpath('//*[@class="table table-bordered table-striped"]//td[2]/text()')

        for i in range(len(ip)):
            #print(ip[i] + ':' + port[i])
            self.r.zadd('proxies',ip[i] + ':' + port[i],'25')
        print('代理5号爬取完成')
    def agent_xiladaili(self):  #获取xiladaili代理
        response = requests.get('http://www.xiladaili.com/',headers=headers)
        data = etree.HTML(response.text)
        ip_port = data.xpath('//*[@class="fl-table"]//td[1]/text()')
        
        for i in range(90):
            #print(ip_port[i])  #调试的时候可以使用打印
            self.r.zadd('proxies',ip_port[i],'25')
        print('代理6号爬取完成')
    def main(self):
        self.agent_xici()       #注：因为互联网的更新太快，如果代码运行不了
        self.agent_31f()        #清注释掉错误的代码
        self.agent_66ip()
        self.agent_89ip()
        self.agent_kuaidaili()
        self.agent_xiladaili()
        print('所有代理爬取完毕')
if __name__ == '__main__':
    Start = agent()
    Start.main()                #启动主程序
