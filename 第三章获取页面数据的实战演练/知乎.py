import requests


headers = {'cookie':'_zap=8ffcdc6d-5a26-45b6-bf79-6bb042d2c247; d_c0="ABDpvkSNXQ-PTigkRsBjvPLRNy20JwM5KU4=|1556756194"; _xsrf=mdOplck90Mhj8TDMWJgqsd7vD6LuRu72; l_n_c=1; q_c1=65b1d2c9a6cf4f57af4e6afd51f11bb9|1557104006000|1557104006000; r_cap_id="NzYzNmUxOTcwYzgzNDYwYmE3ZDA0M2Y3NjNhMWNiNzE=|1557104006|47c6ab0245fa78919dd4d5069f0fe0b2dfd8de37"; cap_id="YjEzNzAyODdkMDc4NDU1OGI4NGFhZTc4NWVhMWI2ZTI=|1557104006|2794f66a9a2680e6f71b1f6557ac65fb68941e26"; l_cap_id="ZjMxN2M3MDBiNzU2NGZlYjk0OGUzZmIyMWExMzE5OTM=|1557104006|7d5377d64dd9d4addc349293860b0d56df433f6c"; n_c=1; __utma=51854390.1232884663.1557104045.1557104045.1557104045.1; __utmb=51854390.0.10.1557104045; __utmc=51854390; __utmz=51854390.1557104045.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20190506=1; tgw_l7_route=7c109f36fa4ce25acb5a9cf43b0b6415; capsion_ticket="2|1:0|10:1557105292|14:capsion_ticket|44:MTViOGE5MzJlZDgxNGE0MGJkOThkN2VhZWU5MGMxYzc=|7d6191e560413b73740aef270aaa153d7b17cf48d6dc733933364b8d65724462"; z_c0="2|1:0|10:1557105302|4:z_c0|92:Mi4xaXhuRUN3QUFBQUFBRU9tLVJJMWREeVlBQUFCZ0FsVk5sdGk4WFFCd1lvM3N6a1EzYVVfaEdFSl9pVG1zSHJGX1dB|0d5a71655ee49539d05993981441733815d1fbf2c9efe0ba176ec46e832bc9d9"',
'referer':'https://www.zhihu.com/signin?next=%2F',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36'}

response = requests.get('https://www.zhihu.com/',headers=headers)
print('添加后headers的状态吗为：'+ str(response.status_code))


f = open('知乎.txt','a',encoding='utf-8')
f.write(response.text)


