import requests
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
    print(each)
file = open("v2ray.txt",'w')
file.write(each)
file.close()
