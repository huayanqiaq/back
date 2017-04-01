import csv
import re
import sys
repace=re.compile('^([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])\.([1-9]?\d|1\d\d|2[0-4]\d|25[0-5])$')
f1=open('666.txt','w')
filename=sys.argv[1]
with open(filename,'rb') as file:
    filecsv=csv.reader(file)
    for line in filecsv:
        if "HK" in line[2]:
            if repace.match(line[0]) and repace.match(line[1]) is not None:
                linecontent=line[0]+"----"+line[1]+"\n"
                f1.write(linecontent)
            else:
                pass
        else:
            pass
f1.close()
f2=open('123456.txt','w+')
with open('666.txt','r') as f:
    for f1 in f:
        ip=f1.split('----')
        startip=ip[0].split('.')
        endip=ip[1].split('.')
        if startip[1]==endip[1]:
            if startip[2]==endip[2]:
                ip=startip[0]+"."+startip[1]+"."+startip[2]+".0/24"
                f2.write(ip+"\n")
            else:
                for num in range(0,(int(endip[2])-int(startip[2])+1)):
                    ip=startip[0]+"."+startip[1]+"."+str((int(startip[2])+num))+".0/24"
                    f2.write(ip+"\n")
        else:
            for num in range(0,(int(endip[1])-int(startip[1])+1)):
                ip=startip[0]+"."+str((int(startip[1])+num))+".0.0/16"
                f2.write(ip+"\n")
f2.close()