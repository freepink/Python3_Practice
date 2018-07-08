#!/usr/bin/env python3
''' Test for list for statement, by Ron Chang, 7th Jul
'''

a = [str(i)+'*'+str(j)+'='+str(i*j) for i in range(2,10) if i%2 == 0 for j in range(2,10) if j%2 == 0]
print (a)


az_list = []
AZ_list = []
result = []
for i in range(ord('A'),ord('Z')+1):
    AZ_list.append(chr(i))
for j in range(ord('a'),ord('z')+1):
    az_list.append(chr(j))
    result = AZ_list + az_list

result_2 = [chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]
print (result_2)
