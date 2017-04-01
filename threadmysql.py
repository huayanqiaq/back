
#!/usr/bin/python
from __future__ import division
from socket import gethostname;
import threading
import sys
import os
import MySQLdb

class threader(threading.Thread):
	def __init__(self,method):
		threading.Thread.__init__(self)
			self.tx =
			self.method = method
			def run(self):
				run_insert()

	def run_insert():
		sql = "INSERT INTO table (`id`,`A`,`B`,`C`) VALUES (NULL,'0','0','0');")
		try:
			cursor.execute(sql)
			db.commit()
		except:
			print "insert failed"

def init_thread(): backgrounds = []
for db in connections:
logger("Spawning thread: %s"%(db),"d")
quant = tx / THREADS
background = threader(method,quant,db)
background.start()
backgrounds.append(background)
for background in backgrounds:
background.join()

def main():
try:
init_thread()
except:
print "failed to initiate threads"

sys.exit(0)

if __name__ == "__main__":
mysql_host = "localhost" #default localhost
mysql_pass = "pass" #default dbbench
mysql_user = "user" #default dbbench
mysql_port = 3306 #default 3306
mysql_db = "schema" #default dbbench
threads = 4 #must be INT not STR #create connection pool

connections = []
for thread in range(THREADS):
try:
connections.append(MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass, db=mysql_db, port=mysql_port))
except MySQLdb.Error, e:
print "Error %d: %s"%(e.args[0], e.args[1])
sys.exit (1)

main()
