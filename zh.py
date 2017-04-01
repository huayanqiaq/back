from lxml import etree
import requests
import time

f1=open('666123.txt','w')
list1=['css','js','ico','jpg']
def gethtml(url):
    content=requests.get(url).content
    xpath_content=etree.HTML(content)
    url1=xpath_content.xpath('//@href')
    alllist=[]
    for i in url1:
        if "http" in i:
            m=i.split('/')
            m1=i.split('.')
            if uri in m[2] and m1[-1] not in list1:
                #print i
                alllist.append(i)
            else:
                pass
        else:
            pass
    return alllist
if __name__=="__main__":
    uri="w2i.wanmei.com"
    url="http://"+uri
    alllist1=gethtml(url)
    for ii in alllist1:
        alllist2=gethtml(ii)
        for iii in alllist2:
            alllist3=gethtml(iii)
            for iiii in alllist3:
                time.sleep(1)
                alllist4=gethtml(iiii)
                for vali in alllist4:
                    f1.write(vali+"\n")
        print "----------------------------------------------------------------\n"
f1.close()