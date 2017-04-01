from lxml import etree
import requests

file=open('1.txt','w+')
url="http://goods2goods.com/commonuser/getFormUsers.action"
req=requests.get(url=url,timeout=6)
content=req.content.decode('utf-8')
content_xpath=etree.HTML(content)
num=content_xpath.xpath('//tr/td[3]')
for i in num:
    name=i.text.strip()
    file.write(name+"\r\n")

file.close()