import serial
import asyncio
#import websockets

'''`
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root"
    passwd = "Asdf_1234",
    database="myLogDB",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE myLogDB2")
#mycursor.execute("CREATE TABLE my_log1(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), val1 INT(10))")
'''

#print('serial ' + serial.__version__) # Set a PORT Number & baud rate 
port = '/dev/ttyACM0'
#port = 'COM11' 
baudRate = 9600 #baudrate 수정

serialPort= serial.Serial(port,baudRate) 

def Decode(serialLine): 
    serialLineDe = serialLine.decode() 
    serialLineStr = str(serialLineDe)
    
    
    if serialLineStr[0] =='P': #첫문자 검사 B
        data = str(serialLineStr[1:-2])
        temp, humid = data.split(",")
        return float(temp), float(humid)
    else:
        print("Failed")
    
def SerialRead(): # return list [Ard1,Ard2] 
    if serialPort.readable(): 
        readLine = serialPort.readline() 
        code=Decode(readLine)
        print(code)
        '''
        mycursor = mydb.cursor()
        sql = "INSERT INTO my_log1 (name, val1) VALUES (%s, %s)"
        val = (code[0], code[1])
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted") 
        return code 
        '''
    else : 
        print("fail from _Ardread_")
'''
async def send():
    uri = 'ws://192.168.0.16:8080'
    async with websockets.connect(uri) as ws:
        while(True):
            SerialRead(ws)
'''        
while(True):
    SerialRead()