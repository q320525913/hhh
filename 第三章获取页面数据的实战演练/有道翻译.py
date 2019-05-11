import requests


headers = {'Cookie':'OUTFOX_SEARCH_USER_ID=-560995023@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=952622393.1610817; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abckG4tzCcZyr5Fk0-kQw; ___rl__test__cookies=1557110160521',
'Host':'fanyi.youdao.com',
'Origin':'http://fanyi.youdao.com',
'Referer':'http://fanyi.youdao.com/?keyfrom=fanyi.logo',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.11096.400',
'X-Requested-With':'XMLHttpRequest'}

data = {'smartresult':'dict',
'smartresult':'rule',
'i':'哈哈哈',
'from':'AUTO',
'to':'AUTO',
'smartresult':'dict',
'client':'fanyideskweb',
'salt':'15571101605313',
'sign':'7b11f158365dc70b56ea5b4eaac3be6e',
'ts':'1557110160531',
'bv':'b98e60abc905b42b72a363969139238a',
'doctype':'json',
'version':'2.1',
'keyfrom':'fanyi.web',
'action':'FY_BY_REALTlME'}
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
response = requests.post(url,headers=headers,data=data)
print(response.text)
