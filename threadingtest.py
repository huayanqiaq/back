import requests
from threading import activeCount
import threading
import socket
import re
import chardet
import MySQLdb
import IPy
import time

conn = MySQLdb.connect(
	host='localhost',
	port=3306,
	user='root',
	passwd='root',
	db='ceshi',
	charset="utf8",
)

header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
repace_title = re.compile(r'\<title\>(.*?)\<\/title\>')


def gethtml(dst, port):
	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		indicator = cli_sock.connect_ex((dst, port))
		if indicator == 0:
			url1 = "http://" + str(dst) + ":" + str(port) + "/"
			# print url1
			try:
				m = requests.get(url=url1, headers=header, timeout=6)
			except:
				pass
			if m.status_code == requests.codes.ok:
				# m.encoding = 'utf-8'
				webtype = m.headers['Server']
				charset = chardet.detect(m.content)['encoding']
				# print charset
				decode_content = m.content.decode(charset)
				titlelist = repace_title.findall(decode_content)
				# print titlelist[0]
				cur = conn.cursor()
				# print cur
				sql = "insert into scan(id,url,title,htmlcontent,webtype) values(id,'%s','%s','%s','%s')" % (
					url1, titlelist[0],666, webtype)
				# print sql
				cur.execute(sql)
				conn.commit()
				cur.close()


			else:
				pass
		else:
			pass
		cli_sock.close()
	except:
		pass


if __name__ == "__main__":
	gethtml('112.124.1.206',80)
	'''iplistall = []
	ipopen = open('123.txt', 'r')
	iplist = ipopen.readlines()
	for ip1 in iplist:
		ip2 = IPy.IP(ip1)
		for ip3 in ip2:
			iplistall.append(ip3)
	ipopen.close()
	# print type(str(iplistall[5]))
	for ip in iplistall:
		gethtml(str(ip), 80)'''

conn.close()
