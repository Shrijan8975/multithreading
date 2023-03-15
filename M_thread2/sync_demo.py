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
    #Without multithreading
    increment_1()
    increment_4()
    decrement_2()
    decrement_3()
    print("Value of x :",x)


