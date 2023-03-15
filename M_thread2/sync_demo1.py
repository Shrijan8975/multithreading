from threading import Thread
def increment_1():
    global x
    for i in range(1,1000000):
        x+=1

def increment_4():
    global x
    for i in range(1,1000000):
        x+=4

def decrement_2():
    global x
    for i in range(1,1000000):
        x-=2

def decrement_3():
    global x
    for i in range(1,1000000):
        x-=3

if(__name__ == "__main__"):
    #It is a global variable i.e. available to all functions
    global x
    x = 0
    print("Value of x :",x)
    #With multithreading
    t1 = Thread(name="t1",target=increment_1)
    t2 = Thread(name="t2",target=increment_4)
    t3 = Thread(name="t3",target=decrement_2)
    t4 = Thread(name="t4",target=decrement_3)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    #All the threads have finished their job
    print("Value of x :",x)


