#coding:UTF-8
import sys
import subprocess

reload(sys)
sys.setdefaultencoding('utf-8')
iplist=[]
for i in range(0,255):
    for ii in range(0,255):
        ip="107."+str(i)+"."+str(ii)+"."+"103"
        iplist.append(ip)
print len(iplist)
for ip1 in iplist:
    cmd = "curl --silent -H \"Host:lsjdnf.com\" --connect-timeout 3 http://"+ip1+"/portal.php"
    print ip1
    try:
        p2=subprocess.Popen(cmd,shell=True)
        p2.wait()
    except:
        pass
    if (p2.returncode == 0):
        print ip1
        sys.exit(0)
