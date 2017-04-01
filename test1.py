# coding: utf-8
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool

#remote_server = raw_input("Enter a remote host to scan:")
remote_server_ip = "103.235.46.39"
ports = []

print '-' * 60
print 'Please wait, scanning remote host ', remote_server_ip
print '-' * 60


socket.setdefaulttimeout(0.5)

def scan_port(port):
    try:
        s = socket.socket(2,1)
        res = s.connect_ex((remote_server_ip,port))
        if res == 0: # 如果端口开启 发送 hello 获取banner
            print 'Port {}: OPEN'.format(port)
        s.close()
    except Exception,e:
        print str(e.message)



for i in range(1,1025):
    ports.append(i)

# Check what time the scan started
t1 = datetime.now()


pool = ThreadPool(processes = 8)
results = pool.map(scan_port,ports)
pool.close()
pool.join()

print 'Multiprocess Scanning Completed in  ', datetime.now() - t1
