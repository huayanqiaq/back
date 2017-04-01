import sys
import re
path=sys.argv[1]
f1=open('123.txt','w+')
f=open(path)
c_iplist=[]


rez=re.compile(r'\d+\.\d+\.\d+\.')

content=f.readlines()
for ip in content:
	ip1=rez.findall(ip)
	for ip2 in ip1:
		c_iplist.append(ip2)

c_iplist1=list(set(c_iplist))
for ip3 in c_iplist1:
	f1.write(ip3+"0"+"/24"+"\r\n")
		
f.close()
f1.close()

		
		




# while (line):
    # line = f.readline() 
    # ip2=re.findall(r'\d+\.\d+\.\d+\.',line)
    # c_iplist.append(ip2)
# else:
	# pass

# iplist=[]
# iplist1=[]
# f=open(path2,'a')
# for line in c_iplist:
    # print line
    # ip=re.findall(r'\d+.\d+.\d+.',line)
    # iplist.append(ip[0])
# for ip in iplist:
    # print ip
    # if ip not in iplist1:
        # iplist1.append(ip)
# for ip in iplist1:
    # for i in range(1,255):
        # print ip
        # ip1=ip+str(i)+'\n'
        # f.write(ip1)