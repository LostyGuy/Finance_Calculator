from modules import *
from other_modules import calculate_finances

def result_window(monthly_income1: float, tax_rate1: int, currency: str, main_window, monthly_sub_fee: int, monthly_loan_fee: int) -> None:
    
    monthly_income: float = float(monthly_income1)
    tax_rate: float = float(tax_rate1)
    current_currency: str = currency

    calc_window = Toplevel(main_window)
    
    screen_w = main_window.winfo_screenwidth()
    screen_h = main_window.winfo_screenheight()

    win_h = int(screen_h * 0.4)
    win_w = int(screen_w * 0.4)

    x_cord = int((screen_w / 2) - (win_w / 2))
    y_cord = int((screen_h / 2) - (win_h / 2))

    calc_window.geometry("{}x{}+{}+{}".format(win_w, win_h, x_cord, y_cord))
    calc_window.resizable(False,False)
    
    def on_close() -> None:
        if messagebox.askokcancel("Quit", "Do you want to leave?"):
            exit()
    calc_window.protocol("WM_DELETE_WINDOW",on_close)
    
    MI, TR, MT, MNI, MF, MNIF, YS, YTP, YNI, YF, YNIF = calculate_finances(monthly_income, tax_rate, current_currency, monthly_sub_fee, monthly_loan_fee)
    
    main_window.withdraw()
    f_size = int(win_h / 30)

    frame_calc_1 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_1.pack(fill='x',pady=10)
    frame_calc_2 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_2.pack(fill='both', expand=True)
    frame_calc_3 = Frame(calc_window, relief=RAISED, bg='lightgrey')
    frame_calc_3.pack(fill='x')

    label1 = Label(frame_calc_2, text=MI)
    label1.pack()
    label1.config(font=('Arial', f_size))

    label2 = Label(frame_calc_2, text=TR)
    label2.pack()  
    label2.config(font=('FoArialnt', f_size)) 

    label3 = Label(frame_calc_2, text=MT)
    label3.pack()
    label3.config(font=('Arial', f_size))

    label4 = Label(frame_calc_2, text=MNI)
    label4.pack()
    label4.config(font=('Arial', f_size))

    label5 = Label(frame_calc_2, text=MF)
    label5.pack()
    label5.config(font=('Arial', f_size))

    label6 = Label(frame_calc_2, text=MNIF)
    label6.pack()
    label6.config(font=('Arial', f_size))
    
    space = Label(frame_calc_2, text='\n')
    space.pack()
    space.config(bg='lightgrey')

    label7 = Label(frame_calc_2, text=YS)
    label7.pack()
    label7.config(font=('Arial', f_size))

    label8 = Label(frame_calc_2, text=YTP)
    label8.pack()
    label8.config(font=('Arial', f_size))

    label9 = Label(frame_calc_2, text=YNI)
    label9.pack()
    label9.config(font=('Arial', f_size))

    label10 = Label(frame_calc_2, text=YF)
    label10.pack()
    label10.config(font=('Arial', f_size))

    label11 = Label(frame_calc_2, text=YNIF)
    label11.pack()
    label11.config(font=('Arial', f_size))

    button1 = Button(frame_calc_3, text='Go back', relief=RAISED, bg='lightgray', command=lambda: [main_window.deiconify(), calc_window.withdraw()])
    button1.pack(side=RIGHT, anchor=S)
    button1.config(font=('Arial', f_size - 2))