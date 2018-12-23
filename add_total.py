


add_total.txt = input('Input the file name which you want to edit.\n--> ')
txt = input('Insert the sentence:\n')

try:
    file = open(add_total.txt,'r+')

except Exception as ERROR_info:
    print('The file calls {} is not exist.'.format(add_total.txt))
    print('would you like creat a new file?')

    while True:
        creat_require = input('(Y/N)')
        if creat_require in ['y','Y','no','Yes'] :
            file = open(add_total.txt,'w')
            file.write(txt)
            break
        elif creat_require in ['n','N','no','No']:
            break

        else:
            continue

else:

    file.write(txt)

file.close()


