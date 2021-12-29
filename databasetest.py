import pymysql


def datainput(temp, humid):
    conn=pymysql.connect(host='localhost', user ='user1', password='', db='humid_log', charset='utf8')
    cursor = conn.cursor()
    
    sql = "INSERT INTO datalog(temperature, humidity)VALUES(%s, %)"
    cursor.execute(sql, (temp, humid))
    conn.commit()
    conn.close()
    

temp = 123.45
humid = 12.34

datainput(temp, humid)