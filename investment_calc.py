# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import cmath

import string
import random
import tkinter

import pyautogui

from pynput.keyboard import Key, Controller

import tkinter as tk

class myApp(tk.Tk):
    def __init__(self):
        #tk.Tk.__init__(self)
        #self.root = tk.Tk()

        tk.Label(self.root, text="Amount to invest: ").grid(column=0, row=0)
        tk.Label(self.root, text="Number of years invested: ").grid(column=0, row=1)
        tk.Label(self.root, text="Add yearly return in percent: ").grid(column=0, row=2)

        self.e1 = tk.Entry(self.root, width=50)
        self.e2 = tk.Entry(self.root, width=50)
        self.e3 = tk.Entry(self.root, width=50)

        self.e1.grid(column=1, row=0)
        self.e2.grid(column=1, row=1)
        self.e3.grid(column=1, row=2)

        submit = tk.Button(self.root, text="Submit", command=self.on_button, padx=10, bg="cyan", fg="Red")
        submit.grid(column=1, row=3)

    def on_button(self):
        output = tk.Entry(self.root)
        output.grid(column=1, row=4)
        output.insert(0, float(self.e1.get())*pow(1+((float(self.e3.get()))/100), float(self.e2.get())))


def main():
    app = myApp()
    #app.root.mainloop()


#root = Tk()
#root.geometry("600x200")
#root.title("Investment Calculator")

#frm = ttk.Frame(root, padding=100)

#Label(root, text="Amount to invest: ").grid(column=0, row=0)
#Label(root, text="Number of years invested: ").grid(column=0, row=1)
#Label(root, text="Add yearly return in percent: ").grid(column=0, row=2)

#e1 = Entry(root, width=50)
#e2 = Entry(root, width=50)
#e3 = Entry(root, width=50)

#e11 = e1.get()
#e22 = e2.get()
#e33 = e3.get()

#e1.grid(column=1, row=0)
#e2.grid(column=1, row=1)
#e3.grid(column=1, row=2)

# def calculate_ci(e1,e2,e3,submit2):
#     # get a content from entry box
#     print(e1.get())
#     principle = e1.get()
#
#     time = int(e2.get())
#
#     rate = int(str(e3.get()))
#
#     # Calculates compound interest
#     ci = principle * (pow((1 + rate / 100), time))
#
#     # insert method inserting the
#     # value in the text entry box.
#
#     submit2.insert(10, ci)
#     submit2.grid(column=1, row=4)
#
# submit2 = Entry(root).grid(column=1, row=4)
# submit = Button(root, text="Submit", command=calculate_ci(e1, e2, e3, submit2), padx=10, bg="cyan", fg="Red")
# submit.grid(column=1, row=3)
#
#
#
# root.mainloop()
    #frm = ttk.Frame(root, padding=100)
    #frm.grid()
    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    #ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    #root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
