import requests
import redis
from random import choice
import threading
from time import time

r = redis.Redis()
code = [200,303]                                        #能成功访问页面的状态码
list1 = []
def Detection_agent(name=None):
    for i in range(3):                                   #获取110分以内的ip
        proxy = choice(r.zrange('proxies',0,110)).decode('utf-8')
                                                        #分数大于0就继续检测ip
        if r.zscore('proxies',proxy) > 0:
            proxies = {'http':'http://'+proxy,'https':'https://'+proxy}
            try:
                response = requests.get('https://www.baidu.com/',proxies=proxies,timeout=30)
                print('获取的状态码为',response.status_code)
                if response.status_code in code:
                    if r.zscore('proxies',proxy) > 100: 
                        r.zadd('proxies',proxy,100)     #把100设置为上限
                    else:
                        r.zincrby('proxies',proxy,10)   #成功获取一次就加10分
                        print('Thread-' + str(name)+'代理',proxy,'成功获取页面,现在分数为',r.zscore('proxies',proxy))
                else:
                    print('获取状态码不对',response.status)
                    r.zincrby('proxies',proxy,-2)       #状态码不对减2分
            except Exception as e:
                r.zincrby('proxies',proxy,-3)           #获取失败减3分
                print('Thread-' + str(name)+'莫名其妙的错误,代理',proxy,'的分数为',r.zscore('proxies',proxy))                
        else:
            r.zrem('proxies',proxy)                     #分数小于等于0就删除代理
            print('成功删除代理',proxy)

t1 = time()
thread_list =  []
for i in range(1,6):
    t = threading.Thread(target=Detection_agent,args=(i,))
    t.start()
    thread_list.append(t)
for thread in thread_list:
    thread.join()
t2 = time()
print('多线程执行15次需要'+str(t2-t1)+'秒')






