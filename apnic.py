import re
repace=re.compile(r'apnic\|CN\|ipv4\|(.*?)\|')
f=open('apnic.txt','r')
iptxt=open('iplist.txt','w')
for linetxt in f.readlines():
    m=repace.findall(linetxt)
    for i in m:
        if i[0] is not None:
            list1=i.split('.')
            if list1[1]=="0" and list1[2]=="0":
                iptxt.write(i+"/8\n")
            elif list1[2]=="0":
                iptxt.write(i+"/16\n")
            else:
                iptxt.write(i+"/24\n")
        else:
            pass
f.close()
iptxt.close()