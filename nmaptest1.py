#coding=utf-8
import socket
import requests
from lxml import etree
import threading
import Queue



def getip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception,e:
        print e

def gethtml(url):
    header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
    try:
        req=requests.get(url,headers=header,timeout=6)
        content=req.content
        content_xpath=etree.HTML(content)
        title=content_xpath.xpath('//head/title')[0].text
        #print req.headers,title
        return (title,req.status_code,req.headers['Server'])
        #print req.headers['Content-Type']
    except Exception,e:
        print e

class scanport(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.ip=ip
    def run(self):
        while not q_queue.empty():
            try:
                #print "test"
                cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                cli_sock.settimeout(1)
                address=q_queue.get()
                indicator = cli_sock.connect_ex(address)
                if indicator == 0:
                    print address
                else:
                    pass
                cli_sock.close()
            except Exception,e:
                print Exception,e

if __name__=="__main__":
    #portlist=[80,4848,7001,7002,8000,8001,8080,8081,8888,9999,9043,9080]
    q_queue=Queue.Queue()
    iplist=[]
#WEB信息的采集
    with open('ip.txt','r') as f:
        for domain in f:
            domain=domain.rstrip()
            url="http://"+domain
            f=gethtml(url)
            ip=getip(domain)
            iplist.append(ip)
            try:
                print domain+"----"+str(ip)+"----"+str(f[1])+"----"+f[2]+"----"+f[0]
            except Exception,e:
                print e
            #print domain+"----"+str(ip)+"----"+str(f[1])
#加入队列扫描任务
    for ip1 in iplist:
        for num in range(1,1000):
            troub=(str(ip1),int(num))
            q_queue.put(troub)   #以元祖的形式把要扫描对象加入队列
    threads=[]                   #存储线程对象
#开始多线程扫描
    for threadnum in range(50):    #固定开启线程数
        t=scanport()
        t.setDaemon(True)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

