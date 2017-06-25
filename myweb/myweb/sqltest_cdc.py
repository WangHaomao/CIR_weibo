# -*- coding:utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def cdc_query(province):

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
    # province = "上海"
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='predictData',port=3306,charset="utf8")
    cur=conn.cursor()
    query = ["SELECT num FROM CDCdata WHERE province = '" + province +"' && sick = '流行性感冒' && month(date('","')) = month(time)"]
    print query
    num = []
    for i in range(len(querytime)):
      cur.execute(query[0] + querytime[i] + query[1])
      data = cur.fetchone()
      if data is None:
        num.append(0)
      else :
        num.append( data[0])

    ss = ["data:["]

    for i in range(len(num)):
      # print num[i],
      ss.append(str(num[i]))
      if i != len(num)-1:
        # print ",",
        ss.append(",")
    # print "],"
    ss.append("],")

    str_ss = "".join(ss)
    return str_ss


if __name__ == '__main__':
    print cdc_query(u"北京")