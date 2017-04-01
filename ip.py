f=open('454654.txt','r')
f1=f.readlines()
for i in f1:
	list=i.split('.')
	print str(list[0])+"."+str(list[1])+"."+str(list[2])+"."+"0/24"

