#coding:utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='root',
        db ='ceshi',
        )
cur = conn.cursor()
print cur
#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
title="jdhfjdshkfjhdkjsh"
url1="http://454.564.54..545.4"
html="dskgjdlkfjgkfdjklg"
webtype="sdkghdskjhgk"
sql="insert into scan(url,title,htmlcontent,webtype) values('%s','%s','%s','%s')" % (url1,title,html,webtype)
print sql
m=cur.execute(sql)
print m


cur.close()
conn.commit()
conn.close()