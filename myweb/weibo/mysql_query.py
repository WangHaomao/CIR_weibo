# -*- coding:utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def province_query():

    province = ['青岛',
                '西藏',
                '上海',
                '福建',
                '广西',
                '广东',
                '山西',
                '云南',
                '辽宁',
                '宁夏',
                '江西',
                '吉林',
                '青海',
                '内蒙古',
                '四川',
                '陕西',
                '重庆',
                '江苏',
                '贵州',
                '北京',
                '新疆',
                '浙江',
                '山东',
                '海南',
                '甘肃',
                '天津',
                '河南',
                '黑龙江',
                '河北',
                '湖南',
                '安徽',
                '湖北'
                ]

    num = []
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='predictData', port=3306, charset="utf8")
    cur = conn.cursor()
    query = [
        "SELECT COUNT(*)  FROM `analyzedWeibo` LEFT JOIN userinfo ON analyzedWeibo.ID = userinfo.ID WHERE lable = 1 && userinfo.city = \"",
        "\" GROUP BY userinfo.city"]

    for i in range(len(province)):
        # print query[0] + province[i] + query[1]
        cur.execute(query[0] + province[i] + query[1])
        data = cur.fetchone()
        if data is None:
            num.append(0)
        else:
            num.append(data[0])
    ss = ["var data = [\n"]

    for i in range(len(province)):
        # print i
        ss.append("{name: '" + province[i] + "', value: " + str(num[i]) + "},\n")

    ss.append('];')

    res =  ''.join(ss)

    cur.close()
    conn.close()
    return res

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


def pro_query(province):
    querytime = ['2016-01-01',
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
    # province = u"湖南"
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='predictData', port=3306, charset="utf8")
    cur = conn.cursor()
    query = [
        "SELECT COUNT(*)  FROM analyzedWeibo LEFT JOIN userinfo ON analyzedWeibo.ID = userinfo.ID WHERE lable = 1 && userinfo.city = '" + province + "' && month(date('",
        "')) = month(pubTime) GROUP BY userinfo.city"]
    num = []
    for i in range(len(querytime)):
        cur.execute(query[0] + querytime[i] + query[1])
        data = cur.fetchone()
        if data is None:
            num.append(0)
        else:
            num.append(data[0] * 111)
    ss = ["data:["]
    for i in range(len(num)):
        # print num[i],
        ss.append(str(num[i]))
        if i != len(num) - 1:
            ss.append(',')
    ss.append("],")
    cur.close()
    conn.close()
    return ''.join(ss)
if __name__ == '__main__':

    print pro_query('湖南')
