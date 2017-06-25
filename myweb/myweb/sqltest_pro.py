# -*- coding:utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


querytime = [ '2016-01-01',
              '2016-02-01',
              '2016-03-01',
              '2016-04-01',
              '2016-05-01',
              '2016-06-01',
              '2016-07-01',
              '2016-08-01',
              '2016-09-01',
              '2016-10-01',
              '2016-11-01',
              '2016-12-01'
              ]
province = "湖南"
conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='predictData',port=3306,charset="utf8")
cur=conn.cursor()
query = ["SELECT COUNT(*)  FROM analyzedWeibo LEFT JOIN userinfo ON analyzedWeibo.ID = userinfo.ID WHERE lable = 1 && userinfo.city = '"+province+"' && month(date('","')) = month(pubTime) GROUP BY userinfo.city"]
num = []
for i in range(len(querytime)):
  cur.execute(query[0] + querytime[i] + query[1])
  data = cur.fetchone()
  if data is None:
    num.append(0)
  else :
    num.append( data[0])
print "data:[",
for i in range(len(num)):
  print num[i],
  if i != len(num)-1:
    print ",",
print "],"
