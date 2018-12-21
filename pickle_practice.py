import pickle
import ron

a_dict = {'da':111, 2:[23,1,4],'23':{1:2,'d':'ssad'}}
'''
file = open('pickle_example.pickle','wb')

pickle.dump(a_dict, file)

file.close()
'''




'''
file = open('pickle_example.pickle','rb')

a_dict1 = pickle.load(file)
file.close()
print(a_dict1)
ron.cmpr(a_dict,a_dict1)
'''

#與第二段結果相同, 不要求file.close()
with open('pickle_example.pickle','rb') as file:

    a_dict1 = pickle.load(file)

print(a_dict1)
ron.cmpr(a_dict,a_dict1)
