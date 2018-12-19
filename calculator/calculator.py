import tkinter as tk

window = tk.Tk()
window.title('Hi')
window.geometry('200x200')

class calculator:

    def add(self, x, y):
        result = x+y
        print(result)

    def minus(self, x, y):
        result = x-y
        return result

    def times(self, x, y):
        result = x*y
        return result

    def divide(self, x, y):
        result = x/y
        return result

var1 = 12
var2 = 5
hey = calculator.add(var1,var2)


b1 = tk.Button(window, text='+',command=hey())

b1.pack()


window.mainloop()
