from tkinter import *
from tkinter import ttk #styles
import tkinter as tk
from tkinter import messagebox

def calulate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

#   |,.2f| Will round the number to two places after point
    global text1,text2,text3,text4,text5,text5,text6,text7

    text1 = (f'Montly income: {currency} {monthly_income: ,.2f}')
    text2 = (f'Tax rate: {tax_rate:,.0f}%')
    text3 = (f'Monthly tax: {currency} {monthly_tax:,.2f}')
    text4 = (f'Monthly net income: {currency} {monthly_net_income:,.2f}')
    text5 = (f'Yearly salary: {currency} {yearly_salary:,.2f}')
    text6 = (f'Yearly tax to pay: {currency} {yearly_tax:,.2f}')
    text7 = (f'Yearly net income: {currency} {yearly_net_income:,.2f}')
    print('Output has been sent')
    

def main() -> None:

    try:
        monthly_income = float(monthly_income1.get())
        tax_rate = float(tax_rate1.get())
    except:
       messagebox.showerror('Data type error', 'Wrong data given!')
       return None

    calc_window = Toplevel(main_window)
    calc_window.geometry('520x400')
    calc_window.resizable(False,False)
    
    calulate_finances(monthly_income, tax_rate, currency = "$")

    main_window.withdraw()
    #main_window.deiconify()

    frame_calc_1 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_1.pack()
    frame_calc_2 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_2.pack()
    frame_calc_3 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_3.pack()

    label1 = Label(frame_calc_2, text=text1)
    label1.pack()
    label2 = Label(frame_calc_2, text=text2)
    label2.pack()
    label3 = Label(frame_calc_2, text=text3)
    label3.pack()
    label4 = Label(frame_calc_2, text=text4)
    label4.pack()
    label5 = Label(frame_calc_2, text=text5)
    label5.pack()
    label6 = Label(frame_calc_2, text=text6)
    label6.pack()
    label7 = Label(frame_calc_2, text=text7)
    label7.pack()

    button1 = Button(frame_calc_3, text='Go back', relief=RAISED, bg='lightgray', command=lambda: [main_window.deiconify(), calc_window.withdraw()])
    button1.pack(side=LEFT)


#   This will prevent script from running if executed from another file, will work only if executed in this file

#if __name__ ==  '__main__':
#    main()

#   Begining of TKinter Window  #

main_window = tk.Tk()
main_window.title('Financial Calculator')
main_window.geometry('520x400')
main_window.resizable(False,False)

frame1 = Frame(main_window,relief=RAISED, name='header')
frame1.pack(fill='x')
frame2 = Frame(main_window,relief=RAISED, name='body')
frame2.pack(fill='x')
frame3 = Frame(main_window,relief=RAISED, name='footer')
frame3.pack(fill='x')

def on_entry_click1(event):
   if monthly_income1.get() == 'Enter your monthly salary':
      monthly_income1.delete(0, tk.END)
      monthly_income1.configure(foreground="black")

def on_focus_out1(event):
   if monthly_income1.get() == "":
      monthly_income1.insert(0, 'Enter your monthly salary')
      monthly_income1.configure(foreground="gray")

def on_entry_click2(event):
   if tax_rate1.get() == 'Enter your tax rate':
      tax_rate1.delete(0, tk.END)
      tax_rate1.configure(foreground="black")

def on_focus_out2(event):
   if tax_rate1.get() == "":
      tax_rate1.insert(0, 'Enter your tax rate')
      tax_rate1.configure(foreground="gray")

title = Label(frame1, text='Welcome to the Calculator', bg='lightblue')
title.pack(fill='x')
title.config(font=('Font', 25))

monthly_income1 = Entry(frame2)
monthly_income1.insert(0, 'Enter your monthly salary')
monthly_income1.bind("<FocusIn>", on_entry_click1)
monthly_income1.bind("<FocusOut>", on_focus_out1)
monthly_income1.pack()

tax_rate1 = Entry(frame2)
tax_rate1.insert(0, 'Enter your tax rate')
tax_rate1.bind("<FocusIn>", on_entry_click2)
tax_rate1.bind("<FocusOut>", on_focus_out2)
tax_rate1.pack()

calc_start = Button(frame2, text='Take me to the Calculator',  command=main)
calc_start.pack()
calc_start.config(font=('font', 10))

main_window.mainloop() #   creates visual window