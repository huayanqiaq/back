import pygeoip
import csv

f=open('ip.txt','w')
gi = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

with open('123.csv','rb') as file:
    filecsv=csv.reader(file)
    for line in filecsv:
        location = gi.record_by_addr(line[0])
        #print location
        if location:
            if location['country_code']=="HK":
                f.write(line[0]+"\n")
            else:
                pass
        else:
            pass
f.close()