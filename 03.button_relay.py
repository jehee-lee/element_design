from tkinter import *
import RPi.GPIO as GPIO
import threading

relay = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)

def relay_trig():
    global relay
    GPIO.output(relay, not GPIO.input(relay))
    print(GPIO.input(relay))
    Entry_state.delete(0, END)
    if GPIO.input(relay) == 1:
        Entry_state.insert(0, "       OPENED")
    elif GPIO.input(relay) == 0:
        Entry_state.insert(0,"       CLOSED")

    
    
try:
    root = Tk()
    menu=Menu(root)
    #초기화
    root.title("element_ design")
    root.geometry("640x300")
    
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
    root.mainloop()


except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()