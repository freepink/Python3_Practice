a = input('please input a:')
b = input('please input b:')

stra = str(a)
strb = str(b)

for i in range(len(stra)):
    if stra[i]=='.':
        x = i+1
for j in range(len(strb)):
    if strb[j]=='.':
        y = j+1

ga = len(stra) - x
gb = len(strb) - y

#if the last number of this float it can be divie by 2 we call it is "even"

if a*(10**ga)% 2 == 0:
    print ("a is even!")
    
else:
    print("a is odd!")

if b*(10**gb)% 2 == 0:
    print("b is even!")

else:
    print("b is odd!")