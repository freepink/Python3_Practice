import tkinter as tk

window = tk.Tk()
window.title('MISURU by Ron')
window.geometry('150x80')

var = tk.StringVar()
var_2 = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='orange', font=('Arial', 12), width=18, height=2)

l.pack()

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('MISURU~ MISURU~')
        var_2.set('Again!')
    else:
        on_hit = False
        var.set('')
        var_2.set('MISURU?')


b = tk.Button(window, text='MISURU?', textvariable=var_2, width=15, height=2, command=hit_me)

b.pack()

window.mainloop()
