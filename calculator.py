from tkinter import *
from tkinter import ttk
import math
root = Tk()
root.title('Calculator')
root.geometry('357x350')
root.resizable(False, False)
root.configure(background='black')
class calculator:
    def __init__(self):
        self.equation = StringVar()
        self.entry_value = ''
        Entry(root, width=100, font=('Arial', 50), textvariable=self.equation, background='gray', foreground='black').place(x=0, y=0, height=100)
        #Buttons for the values
        Button(root, width=11, height=-4, relief=FLAT, text='(', background='gray', foreground='Black', command=lambda:self.show('(')).place(x=0, y=110)
        Button(root, width=11, height=-4, relief=FLAT, text=')', background='gray', foreground='Black', command=lambda:self.show(')')).place(x=90, y=110)
        Button(root, width=10, height=-4, relief=FLAT, text='%', background='gray', foreground='Black', command=lambda:self.show('%')).place(x=180, y=110)
        Button(root, width=11, height=-4, relief=FLAT, text='1', background='gray', foreground='Black', command=lambda:self.show('1')).place(x=0, y=145)
        Button(root, width=11, height=-4, relief=FLAT, text='2', background='gray', foreground='Black', command=lambda:self.show('2')).place(x=90, y=145)
        Button(root, width=10, height=-4, relief=FLAT, text='3', background='gray', foreground='Black', command=lambda:self.show('3')).place(x=180, y=145)
        Button(root, width=11, height=-4, relief=FLAT, text='4', background='gray', foreground='Black', command=lambda:self.show('4')).place(x=0, y=180)
        Button(root, width=11, height=-4, relief=FLAT, text='5', background='gray', foreground='Black', command=lambda:self.show('5')).place(x=90, y=180)
        Button(root, width=10, height=-4, relief=FLAT, text='6', background='gray', foreground='Black', command=lambda:self.show('6')).place(x=180, y=180)
        Button(root, width=11, height=-4, relief=FLAT, text='7', background='gray', foreground='Black', command=lambda:self.show('7')).place(x=0, y=215)
        Button(root, width=10, height=-4, relief=FLAT, text='9', background='gray', foreground='Black', command=lambda:self.show('9')).place(x=180, y=215)
        Button(root, width=11, height=-4, relief=FLAT, text='0', background='gray', foreground='Black', command=lambda:self.show('0')).place(x=90, y=250)
        Button(root, width=11, height=-4, relief=FLAT, text='8', background='gray', foreground='Black', command=lambda:self.show('8')).place(x=90, y=215)
        Button(root, width=10, height=-4, relief=FLAT, text='.', background='gray', foreground='Black', command=lambda:self.show('.')).place(x=180, y=250)
        Button(root, width=11, height=-4, relief=FLAT, text='+', background='gray', foreground='Black', command=lambda:self.show('+')).place(x=267, y=180)
        Button(root, width=11, height=-4, relief=FLAT, text='-', background='gray', foreground='Black', command=lambda:self.show('-')).place(x=267, y=215)
        Button(root, width=11, height=-4, relief=FLAT, text='/', background='gray', foreground='Black', command=lambda:self.show('/')).place(x=267, y=110)
        Button(root, width=11, height=-4, relief=FLAT, text='*', background='gray', foreground='Black', command=lambda:self.show('*')).place(x=267, y=145)
        Button(root, width=11, height=-4, relief=FLAT, text='=', background='gray', foreground='Black', command=self.solve).place(x=267, y=250)
        Button(root, width=10, height=-4, relief=FLAT, text='C', background='gray', foreground='Black', command=self.clear).place(x=3, y=250)
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)
    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)

calculator()
root.mainloop()