import re
f=open('45654.txt','r')
f1=open('111.txt','wb')
content=f.read()
r=re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d')
list1=re.findall(r,content)
#print list1
for i in list1:
	f1.write("a"+i+"----"+i+"\r\n")
f.close()
f1.close()
