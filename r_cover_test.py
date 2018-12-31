import sys
import time

Az_list = [chr(i) for i in range(ord('A'),ord('Z')+1)]+[chr(i) for i in range(ord('a'),ord('z')+1)]

for i in Az_list:

    x = '\t'+ str(i) + '\r'
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.01)
print('\nDone!')
