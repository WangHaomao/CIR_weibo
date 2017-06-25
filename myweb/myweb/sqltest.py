# -*- coding:utf-8 -*-
import MySQLdb
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

if __name__ == '__main__':
    print province_query()
