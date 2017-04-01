from lxml import etree

f2=open('1234.txt','w+')
f=open('123.html','r+').read()
xf1=etree.HTML(f)
#print xf1
m=xf1.xpath('//a')
for i in m:
	f2.write(i.text+"\r\n")

