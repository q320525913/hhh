import requests
import json

def getjson():
    url = 'http://api.map.baidu.com/panorama/v2?'
    
    pa = {'ak':'1eHRqys109MfLs4P3oA22qKXieLdKfh3',
          'width':'512',
          'height':'256',
          'location':'113.30974633009278,23.149826060892928',
          'fov':'180'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    r = requests.get(url,params=pa,headers=headers)
    with open('123.jpg','wb')as f:
        f.write(r.content)

getjson()


#每个账号一天只有2000次的调用限额，如果进行了认证一天就会有10万次的调用限额

'''
参数      是否必须     默认值        含义
ak          是          无            用户的访问密钥。只支持浏览器端ak和Android/
                                     IOS SDK的ak，服务端ak不支持sn校验方式。
location    是	       无	      全景位置点坐标。坐标格式：lng<经度>，
                                     lat<纬度>，例如116.313393,40.047783。
poiid	    是	       无	     poi的id，该属性通常通过place api接口获取，poiid与
                                     panoid、location一起设置全景的显示场景，优先级为：
                                     poiid>panoid>location。其中根据poiid获取的全景视角最佳。
panoid	    是	       无	      全景图id，panoid与poiid、location一起设置全景的显示场景，
                                     优先级为：poiid>panoid>location。
mcode	    否	        无	      安全码。若为Android/IOS SDK的ak, 该参数必需。
width	    否	       400	      图片宽度，范围[10,1024]
height	    否	       300	      图片高度，范围[10,512]
coordtype   否	      bd09ll	      全景位置点的坐标类型，目前支持bd09ll（百度坐标），
                                     wgs84ll（GPS坐标）和gcj02（google，高德，soso坐标）。
heading	    否	        0	     水平视角，范围[0,360]
pitch	    否	        0	     垂直视角，范围[0,90]。
fov	    否	       90	     水平方向范围，范围[10,360]，fov=360即可显示整幅全景图
'''
#文档地址：https://lbsyun.baidu.com/index.php?title=viewstatic

