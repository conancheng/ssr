import requests
import base64
import random
import lxml
#import io
from lxml import etree
# 获取源码
html = requests.get("https://view.freev2ray.org/")
# 打印源码
#print(html.text)
#提取https://view.freev2ray.org/的V2RAY链接，12小时更新一次
#//*[@id="intro"]/div/div/footer/ul[1]/li[2]/button

etree_html = etree.HTML(html.text)
content = etree_html.xpath('//button[@class="copybtn"]/@data-clipboard-text')
for each in content:
    each
#vmess获取base64加密
str_each = str(each)
b64each = base64.b64encode(str_each.encode('utf-8'))
print(str(b64each,'utf-8'))
str_b64each = str(b64each,'utf-8')
#保存加密后的文件到v2ray.txt
file = open("v2ray.txt",'w')
num = random.randint(0,30)
x = ' '
kongge = num * x
file.write(str_b64each + kongge)
file.close()
file = open("v2ray",'w')
file.write(str_b64each + kongge)
file.close()
