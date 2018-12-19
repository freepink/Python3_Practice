class ExampleClass:
    def __init__(self):
        name = 'example'

    def someFunction(self, a):
        if a >  5:
            return True
        else:
            return False

def separateFunction(b):
    for i in b:
        if i == 1:
            return True
        return False

result = separateFunction([6,5,4,3,2,1])

print(result)
