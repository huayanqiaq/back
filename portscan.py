import socket
import threading
import IPy



#socket.setdefaulttimeout(3)
class scanport(threading.Thread):
    def __init__(self,ip,port):
        threading.Thread.__init__(self)
        self.ip=ip
        self.port=port
    #global iplistall
    def run(self):
        ip1=str(self.ip)
        #port1=self.port
        try:
            cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cli_sock.settimeout(6)
            address=(str(self.ip),int(self.port))
            indicator = cli_sock.connect_ex(address)
            if indicator == 0:
                f.write(ip1+"\n")
                print ip1
            else:
                pass
        except Exception,e:
            print Exception,e
        cli_sock.close()

if __name__=="__main__":
    
    f=open('1234.txt','w')
    port2=80
    with open('123.txt','r') as f1:
        for ip1 in f1:
            iplistall=[]
            ip2=IPy.IP(ip1)
            for ip3 in ip2:
                iplistall.append(ip3)
            threads = []
            #print str(iplistall[0])

            for ip in iplistall:
                threadpage=scanport(ip,port2)
                threads.append(threadpage)
            #print threads[0]
            for t in threads:
                t.start()
                while True:
                    if(len(threading.enumerate())<200):
                        break
            for t1 in threads:
                t1.join()
    f.close()
