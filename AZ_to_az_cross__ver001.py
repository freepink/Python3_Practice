uppercase = []
lowercase = []
for A in range(ord('A'), ord('Z')+1):
    uppercase.append(chr(A))
for a in range(ord('a'), ord('z')+1):
    lowercase.append(chr(a))

for order in range(len(uppercase)):
    A_order = order
    a_order = (26-order)
    if a_order > A_order:
        print ('  '*(order)+uppercase[order]+'  '*(26-order*2)+lowercase[order])
    else:
        print ('  '*(26-order)+lowercase[order]+'  '*(order-13)*2+uppercase[order])
# Method 2 -use while condition to control
