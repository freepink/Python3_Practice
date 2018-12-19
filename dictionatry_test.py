dictionary = {
        'Name' : 'Ron',
        'Age' : '27',
        'Height' : '183',
        'Weight' : '89'
        }

for k in dictionary.keys():

    unit = ''

    if k == 'Age':
        unit = 'years old'
    elif k == 'Height':
        unit = 'cm'
    elif k == 'Weight':
        unit = 'kg'
    else:
        unit = ''

    print('{} is {} {}'. format(k, dictionary[k], unit))


