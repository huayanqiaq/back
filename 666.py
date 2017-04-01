import threading
import Queue
import socket
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
    q_queue=Queue.Queue()
    iplist=['111.206.107.84','111.206.107.79','111.206.107.107','111.206.107.77','111.206.107.85']

    for ip1 in iplist:
        for num in range(1,1000):
            troub=(str(ip1),int(num))
            q_queue.put(troub)
    threads=[]

    for threadnum in range(50):
        t=scanport()
        t.setDaemon(True)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()