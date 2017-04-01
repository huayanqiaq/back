import time
import threading
import requests
import IPy
import re
import chardet
import MySQLdb

visitTimesPerPage = 20
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='ceshi',
        charset="utf8",
        )

header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
repace_title=re.compile(r'\<title\>(.*?)\<\/title\>')
cur = conn.cursor()
threadLock = threading.Lock()
class scanhtml(threading.Thread):
    def __init__(self, threadName, host):
        threading.Thread.__init__(self, name = threadName)
        self.host = host

    global iplistall
    def run(self):
        url = "http://"+str(self.host)+":80/"
        try:
            doc = requests.get(url,headers=header,timeout=3)

            webtype = doc.headers['Server']

            charset=chardet.detect(doc.content)['encoding']
            #print charset
            decode_content = doc.content.decode(charset)
            titlelist=repace_title.findall(decode_content)
            print url
            #cur = conn.cursor()
            sql="insert into scan(id,url,title,htmlcontent,webtype) values(id,'%s','%s','%s','%s')" % (url,titlelist[0],6,webtype)
            #sqllist.append(sql)
            threadLock.acquire()
            try:
                cur.execute(sql)
                conn.commit()
            except:
                conn.rollback()
            threadLock.release()
        except Exception:
            pass

if __name__ =="__main__":
    '''iplistall=[]
    ipopen=open('123.txt','r')
    iplist=ipopen.readlines()
    for ip1 in iplist:
        #print ip1
        ip2=IPy.IP(ip1)
        for ip3 in ip2:
            iplistall.append(ip3)
    ipopen.close()
    threads = []
    for ip in iplistall:
        threadpage=scanhtml(str(time.time()),ip)
        threads.append(threadpage)

    for t in threads:
        t.start()
        while True:
            if(len(threading.enumerate())<200):
                break

    for t1 in threads:
        t1.join()


    conn.close()'''

    
    with open('123.txt','r') as f:
        for ip1 in f:
            iplistall=[]
            ip2=IPy.IP(ip1)
            for ip3 in ip2:
                iplistall.append(ip3)
            threads = []
            for ip in iplistall:
                threadpage=scanhtml(str(time.time()),ip)
                threads.append(threadpage)

            for t in threads:
                t.start()
            while True:
                if(len(threading.enumerate())<200):
                    break

            for t1 in threads:
                t1.join()
    conn.close()