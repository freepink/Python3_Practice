a = input('a:')
#a.isdigit()
#is the same
#a.isnumeric()
if (a.isdigit() == 'True') | (a != '0'):
    print(-int(a))
else:
    print('Error!')
