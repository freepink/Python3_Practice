Az_list = [chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]

for i in range(10):
    for j in Az_list:
        print(j+'__'+str(i)+'\r')

print('Done!')
