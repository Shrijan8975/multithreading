from threading import Thread,Lock
def increment_1():
    global x
    for i in range(1,100000):
        #lock the resource
        lock.acquire()
        x+=1
        #release the resource
        lock.release()

def increment_4():
    global x
    for i in range(1,100000):
        #lock the resource
        lock.acquire()
        x+=4
        lock.release()

def decrement_2():
    global x
    for i in range(1,100000):
        lock.acquire()
        x-=2
        lock.release()

def decrement_3():
    global x
    for i in range(1,100000):
        lock.acquire()
        x-=3
        lock.release()

if(__name__ == "__main__"):
    #It is a global variable i.e. available to all functions
    global x,lock
    lock = Lock()
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


