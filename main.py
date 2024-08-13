from tkinter import *
from tkinter import ttk
import tkinter as tk

def calulate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

#   |,.2f| Will round the number to two places after point
    global text1,text2,text3,text4,text5,text5,text6,text7

    print("-" * 20)
    text1 = (f'Montly income: {currency} {monthly_income: ,.2f}')
    text2 = (f'Tax rate: {tax_rate:,.0f}%')
    text3 = (f'Monthly tax: {currency} {monthly_tax:,.2f}')
    text4 = (f'Monthly net income: {currency} {monthly_net_income:,.2f}')
    text5 = (f'Yearly salary: {currency} {yearly_salary:,.2f}')
    text6 = (f'Yearly tax to pay: {currency} {yearly_tax:,.2f}')
    text7 = (f'Yearly net income: {currency} {yearly_net_income:,.2f}')
    print("-" * 20)
    

def main() -> None:

    calc_window = Toplevel(main_window)
    calc_window.geometry('520x400')
    calc_window.resizable(False,False)

    

    #monthly_income: float = float(input('Enter your monthly salary: '))
    #tax_rate: float = float(input('Enter your tax rate (%): '))

    #main_window.destroy()
    
    calulate_finances(monthly_income, tax_rate, currency = "$")

    main_window.withdraw()
    main_window.deiconify()

    label1 = Label(calc_window, text=text1)
    label1.pack()
    label2 = Label(calc_window, text=text2)
    label2.pack()
    label3 = Label(calc_window, text=text3)
    label3.pack()
    label4 = Label(calc_window, text=text4)
    label4.pack()
    label5 = Label(calc_window, text=text5)
    label5.pack()
    label6 = Label(calc_window, text=text6)
    label6.pack()
    label7 = Label(calc_window, text=text7)
    label7.pack()

#   This will prevent script from running if executed from another file, will work only if executed in this file

#if __name__ ==  '__main__':
#    main()

#   Begining of TKinter Window

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

title = Label(frame1, text='Welcome to the Calculator', bg='lightblue')
title.pack(fill='x')
title.config(font=('Font', 25))

monthly_income = Entry(frame2,)
monthly_income.insert(0, 'Enter your monthly salary')
monthly_income.pack()

tax_rate = Entry(frame2)
tax_rate.insert(0, 'Enter your tax rate')
tax_rate.pack()


calc_start = Button(frame2, text='Take me to the Calculator',  command=main)
calc_start.pack()
calc_start.config(font=('font', 10))


main_window.mainloop() #   creates visual window