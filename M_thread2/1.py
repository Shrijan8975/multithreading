x = 10

def test():
   global x
   x += 11 
   print(x)

print('>>',x)
test()
print('>>',x)
x=20
test()
print('>>',x)

