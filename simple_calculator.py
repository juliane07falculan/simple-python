from tkinter import *

calculator = Tk()

calculator.geometry('400x500')
icon = PhotoImage(file='images/calculator.png')
calculator.iconphoto(True, icon)

label = Label(calculator, text='Simple Calculator')
label.pack()

calc_screen = Label(calculator)
calc_screen.pack()

calc_button_frame = Frame(calculator)
calc_button_frame.pack()

first_row = Button (text= 'ok')
first_row.grid(row=1, column=1)

calculator.mainloop()