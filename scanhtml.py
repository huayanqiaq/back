import requests
import socket
import re
import chardet
import MySQLdb
import IPy

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

def gethtml(dst,port):
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        indicator = cli_sock.connect_ex((dst, port))
        if indicator == 0:
            url1="http://"+str(dst)+":"+str(port)+"/"
            print url1
            try:
                m=requests.get(url=url1,headers=header,timeout=0.3)
            except:
                pass
            if m.status_code == requests.codes.ok:

                webtype = m.headers['Server']
                #headercontent=str(m.headers)
                charset=chardet.detect(m.content)['encoding']
                #print charset
                decode_content = m.content.decode(charset)
                titlelist=repace_title.findall(decode_content)
                #print titlelist[0]
                cur = conn.cursor()
                #print cur
                sql="insert into scan(id,url,title,htmlcontent,webtype) values(id,'%s','%s','%s','%s')" % (url1,titlelist[0],6,webtype)
                #print sql
                cur.execute(sql)
                conn.commit()
                cur.close()


            else:
                pass
        else:
            pass
        cli_sock.close()
    except:
        pass



if __name__ == "__main__":
    #gethtml('112.124.1.206',80)
    iplistall=[]
    ipopen=open('123.txt','r')
    iplist=ipopen.readlines()
    for ip1 in iplist:
        #print ip1
        ip2=IPy.IP(ip1)
        for ip3 in ip2:
            iplistall.append(ip3)
    ipopen.close()

    for ipaddr in iplistall:
        gethtml(str(ipaddr),80)

    conn.close()







