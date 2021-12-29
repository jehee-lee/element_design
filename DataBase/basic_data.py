import pymysql

conn=pymysql.connect(host='localhost', user ='root', password='', db='Humid_log', charset='utf8')
cursor = conn.cursor()

try:

sql=""
cursor = execute(sql,"")

except:
    print("Error")

conn.commit()
conn.close