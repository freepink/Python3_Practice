import itertools

print ('-'*10)
for i, j in itertools.product(range(2,10), range(2,10)):
    print (('%d X %d = %2.d')%(i, j, i*j))
    if j == 9:
        print ('-'*10)
