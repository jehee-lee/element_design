from tkinter import *
import RPi.GPIO as GPIO
import threading
import continuous_threading
import pymysql
import serial

relay = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)
port = '/dev/ttyACM0'
baudRate = 9600 #baudrate 수정
serialPort= serial.Serial(port,baudRate) 


def relay_trig():
    global relay
    GPIO.output(relay, not GPIO.input(relay))
    print(GPIO.input(relay))
    Entry_state.delete(0, END)
    if GPIO.input(relay) == 1:
        Entry_state.insert(0, "       OPENED")
    elif GPIO.input(relay) == 0:
        Entry_state.insert(0,"       CLOSED")

'''
============ database is created as below ============
    MariaDB [humid_log]> CREATE TABLE datalog(
    -> id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -> temperature DECIMAL(5,2),
    -> humidity DECIMAL(5,2),
    -> time DATETIME DEFAULT CURRENT_TIMESTAMP
    -> );
'''

def datainput(temp, humid):
    conn=pymysql.connect(host='localhost', user ='user1', password='', db='humid_log', charset='utf8')
    cursor = conn.cursor()
    
    sql = "INSERT INTO datalog(temperature, humidity)VALUES(%s, %s)"
    cursor.execute(sql, (temp, humid))
    conn.commit()
    
def write_data(temp, humid):
    Entry_temperature.delete(0,END)
    Entry_humidity.delete(0,END)
    Entry_temperature.insert(0,temp)
    Entry_humidity.insert(0,humid)
    
def Decode(serialLine): 
    serialLineDe = serialLine.decode() 
    serialLineStr = str(serialLineDe)
    
    
    if serialLineStr[0] =='P': #첫문자 검사 B
        data = str(serialLineStr[1:-2])
        temp, humid = data.split(",")
        datainput(temp,humid) # input data into DataBase
        write_data(temp,humid)
    
        
        return float(temp), float(humid)
    else:
        print("Failed")
        
def SerialRead(): # return list [Ard1,Ard2] 
    if serialPort.readable(): 
        readLine = serialPort.readline() 
        code=Decode(readLine)
        print(code)
    

    
Thread1=continuous_threading.PeriodicThread(0.005,SerialRead)
    
try:
    root = Tk()
    menu=Menu(root)
    #초기화
    root.title("element_ design")
    root.geometry("640x300")
    
    label_temperature=Label(root, text="temperature")
    label_temperature.place(x = 220, y =50)
    
    Entry_temperature=Entry(root, width = 8)
    Entry_temperature.place(x = 220, y = 80)
    
    label_humidity=Label(root, text="humidity")
    label_humidity.place(x= 225, y = 150)
    
    Entry_humidity=Entry(root, width = 8)
    Entry_humidity.place(x = 220, y=180)
    
    
    label_pipe_state = Label(root, text= "pipe_state")
    label_pipe_state.place(x=520, y = 10)
    
    Entry_state = Entry(root, width = 13)
    Entry_state.place(x=500, y=27)
    Entry_state.insert(0, "       CLOSED")


    btn1 = Button(root, text= "on/off", width=10, height=10, command = relay_trig)
    btn1.place(x = 500, y = 50)

    btn2 = Button(root, text= "Exit", command = root.destroy)
    btn2.place(x = 580, y = 250)

    label_last = Label(root, text= "designed_ by_JH_Lee")
    label_last.place(x= 500, y = 280)
    
    
    Thread1.start()
    root.mainloop()


except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
