from modules import *
from other_modules import calculate_finances
import main

def result_window(monthly_income1: float, tax_rate1: int, currency: str, main_window) -> None:

    monthly_income: float = float(monthly_income1.get())
    tax_rate: float = float(tax_rate1.get())
    current_currency: str = currency.get()

    calc_window = Toplevel(main_window)
    calc_window.geometry('520x400')
    calc_window.resizable(False,False)
    main_window.eval(f'tk::PlaceWindow {str(calc_window)} center')
    
    text1, text2, text3, text4, text5, text6, text7 = calculate_finances(monthly_income, tax_rate, current_currency)

    main_window.withdraw()
    #main_window.deiconify()

    frame_calc_1 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_1.pack(fill='x')
    frame_calc_2 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_2.pack(fill='x')
    frame_calc_3 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_3.pack(fill='x')

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
    button1.pack(side=RIGHT, anchor=S)