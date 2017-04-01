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
        #print req.headers
        return title,req.status_code,req.headers['Server']
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

    with open('ip.txt','r') as f:
        for domain in f:
            domain=domain.rstrip()
            url="http://"+domain
            f=gethtml(url)
            ip=getip(domain)
            iplist.append(ip)
            print domain+"----"+str(ip)+"----"+str(f[1])+"----"+f[2]+"----"+f[0]

    for ip1 in iplist:
        for num in range(1,500):
            troub=(str(ip1),int(num))
            q_queue.put(troub)
    threads=[]
    for threadnum in range(50):
        t=scanport()
        t.start()
        threads.append(t)
    for ii in threads:
        ii.join()

