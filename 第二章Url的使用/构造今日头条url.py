for i in range(11):
	url='https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E9%A3%8E%E6%99%AF&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1557093857314'.format(i*20)
	print(url)
