from modules import *

#   Begining of TKinter Window  #
def main() -> None:
   
   global main_window, monthly_income1, tax_rate1
   
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
   monthly_income1.pack(pady=[10,0])

   tax_rate1 = Entry(frame2)
   tax_rate1.insert(0, 'Enter your tax rate')
   tax_rate1.bind("<FocusIn>", on_entry_click2)
   tax_rate1.bind("<FocusOut>", on_focus_out2)
   tax_rate1.pack(pady=[0,10])

   calc_start = Button(frame2, text='Take me to the Calculator',  command=result_window)
   calc_start.pack()
   calc_start.config(font=('font', 10))

   guidance = Label(frame3, text='Introduction', bg='darkgrey', font='Arial')
   guidance.pack(pady=[10,0], fill='x')

   guidance_description = Label(frame3, text='''
   1. In box with Monthly Salary please enter real or aproximate value to yor earning.
   2. In box with tax rate enter a number before the '%' corresponding with your state or country.
   3. After filling above boxes procced to calculation.
   ''', bg='darkgrey', font=('font', 9) )
   guidance_description.pack(fill='x')

   main_window.eval('tk::PlaceWindow . center')
   main_window.mainloop() #   creates visual window
   
   
def result_window() -> None:

    try:
        monthly_income = float(monthly_income1.get())
        tax_rate = float(tax_rate1.get())
        if monthly_income < 100:
          messagebox.showerror('Invalid Input', 'Make sure your salary is valid and above 100')
          return None
    except ValueError:
       messagebox.showerror('Data type error', 'Please enter only numbers!')
       return None

    calc_window = Toplevel(main_window)
    calc_window.geometry('520x400')
    calc_window.resizable(False,False)
    
    text1, text2, text3, text4, text5, text6, text7 = calculate_finances(monthly_income, tax_rate, currency="$")

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

#   This will prevent script from running if executed from another file, will work only if executed in this file

if __name__ ==  '__main__':
    main()