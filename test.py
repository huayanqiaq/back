import threading
import Queue
import socket


class scanport(threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.ip=ip
    def run(self):
        # while not q_queue.empty():
        #     try:
        #         cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #         cli_sock.settimeout(1)
        #         port1=q_queue.get()
        #         address=(str(self.ip),int(port1))
        #         indicator = cli_sock.connect_ex(address)
        #         if indicator == 0:
        #             print str(self.ip)+":"+str(port1)
        #         else:
        #             pass
        #         cli_sock.close()
        #     except Exception,e:
        #         print Exception,e

q_queue=Queue.Queue()
ip=[111.206.107.84, 111.206.107.79, 111.206.107.107, 111.206.107.77, 111.206.107.85, 111.206.107.80, 111.206.107.82, 111.206.107.81, 111.206.107.83, 111.206.107.78]
for i in ip:
    q_queue.put(i)


