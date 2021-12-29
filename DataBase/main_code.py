import serial
import pymysql
#import websockets

conn=pymysql.connect(host='localhost', user ='root', password='', db='Humid_log', charset='utf8')

#print('serial ' + serial.__version__) # Set a PORT Number & baud rate 
port = '/dev/ttyUSB1'
#port = 'COM11' 
baudRate = 9600 #baudrate 수정

serialPort= serial.Serial(port,baudRate) 

def Decode(serialLine): 
    serialLineDe = serialLine.decode() 
    serialLineStr = str(serialLineDe)
    
    
    if serialLineStr[0] =='P': #첫문자 검사 B
        col_num = str(serialLineStr[1:-2])
        data1, data2 = data.split(",")
        print("data_received")
        return data1, data2
    else : 
        return 'NULL', 'NULL'
        
def SerialRead(): # return list [Ard1,Ard2] 
    if serialPort.readable(): 
        readLine = serialPort.readline() 
        code=Decode(readLine)
        print(code)
        '''
        cursor = conn.cursor()

        sql="INSERT INTO log_data (humid, temperature) VALUES (%s, %s)"
        val = data1, data2
        cursor.execute(sql, val)
        cursor.commit()
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