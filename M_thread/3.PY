import time
import threading

def display():
    data = "FirstBit Solutions"
    for ch in data:
        print(ch, end= " ")
        time.sleep(1)

t1 =  threading.Thread(name = "First", target=display)

t1.start()
display()