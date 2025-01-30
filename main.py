from modules import *
from other_modules import result_window

#   Begining of TKinter Window  #
def main() -> None:

   main_window = tk.Tk()
   main_window.title('Financial Calculator')

   screen_w = main_window.winfo_screenwidth()
   screen_h = main_window.winfo_screenheight()

   win_h = int(screen_h / 2)
   win_w = int(screen_w / 2) - 200


   x_cord = int((screen_w / 2) - (win_w / 2))
   y_cord = int((screen_h / 2) - (win_h / 2))

   main_window.geometry("{}x{}+{}+{}".format(win_w, win_h, x_cord, y_cord))
   main_window.resizable(False, False)

   frame1 = Frame(main_window,relief=RAISED, name='header')
   frame1.pack(fill='x')
   frame3 = Frame(main_window,relief=RAISED, name='description')
   frame3.pack(fill='x', side='top')
   frame2 = Frame(main_window,relief=RAISED, name='body-left')
   frame2.pack(side='left', padx=120, fill='both')
   frame4 = Frame(main_window,relief=RAISED, name='body-right')
   frame4.pack(side='right', padx=120, fill='both')

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
   
   def on_entry_click3(event):
      if monthly_sub_fee1.get() == 'Enter your total monthly subscription expenses':
         monthly_sub_fee1.delete(0, tk.END)
         monthly_sub_fee1.configure(foreground="black")
   def on_focus_out3(event):
      if monthly_sub_fee1.get() == "":
         monthly_sub_fee1.insert(0, 'Enter your total monthly subscription expenses')
         monthly_sub_fee1.configure(foreground="gray")
   
   def on_entry_click4(event):
      if monthly_loan_fee1.get() == 'Enter your monthly loan installment':
         monthly_loan_fee1.delete(0, tk.END)
         monthly_loan_fee1.configure(foreground="black")
   def on_focus_out4(event):
      if monthly_loan_fee1.get() == "":
         monthly_loan_fee1.insert(0, 'Enter your monthly loan installment')
         monthly_loan_fee1.configure(foreground="gray")

   title = Label(frame1, text='Welcome to the Calculator', bg='lightblue')
   title.pack(fill='x')
   title.config(font=('Font', 35))

   monthly_income1 = Entry(frame2, width=25, justify='center')
   monthly_income1.insert(0, 'Enter your monthly salary')
   monthly_income1.bind("<FocusIn>", on_entry_click1)
   monthly_income1.bind("<FocusOut>", on_focus_out1)
   monthly_income1.pack(pady=[10,0])
   monthly_income1.config(font=('Font', 15))

   tax_rate1 = Entry(frame2, width=25, justify='center')
   tax_rate1.insert(0, 'Enter your tax rate')
   tax_rate1.bind("<FocusIn>", on_entry_click2)
   tax_rate1.bind("<FocusOut>", on_focus_out2)
   tax_rate1.pack(pady=[0,10])
   tax_rate1.config(font=('Font', 15))

   monthly_sub_fee1 = Entry(frame4, width=40, justify='center')
   monthly_sub_fee1.insert(0, 'Enter your total monthly subscription expenses')
   monthly_sub_fee1.bind("<FocusIn>", on_entry_click3)
   monthly_sub_fee1.bind("<FocusOut>", on_focus_out3)
   monthly_sub_fee1.pack(pady=[10,0])
   monthly_sub_fee1.config(font=('Font', 15))

   monthly_loan_fee1 = Entry(frame4, width=40, justify='center')
   monthly_loan_fee1.insert(0, 'Enter your monthly loan installment')
   monthly_loan_fee1.bind("<FocusIn>", on_entry_click4)
   monthly_loan_fee1.bind("<FocusOut>", on_focus_out4)
   monthly_loan_fee1.pack(pady=[0,10])
   monthly_loan_fee1.config(font=('Font', 15))

   opt = Label(frame4, text='⬆ Optional Choice ⬆', bg='darkgrey', font='Arial')
   opt.pack(pady=[10,0])
   opt.config(font=('Font', 15))
   
   def checkval() -> None:
      try:
         monthly_income: float = float(monthly_income1.get())
         tax_rate: float = float(tax_rate1.get())
         current_currency: str = currency.get()
         try:
            monthly_sub_fee: float = float(monthly_sub_fee1.get())
         except ValueError:
            monthly_sub_fee1.delete(0, tk.END)
            monthly_sub_fee1.insert(0, '0')
            monthly_sub_fee = 0
         try:
            monthly_loan_fee: float = float(monthly_loan_fee1.get())
         except ValueError:
            monthly_loan_fee1.delete(0, tk.END)
            monthly_loan_fee1.insert(0, '0')
            monthly_loan_fee = 0
         
         if monthly_income < 100:
            messagebox.showerror('Invalid Input', 'Make sure your salary is valid or above 100')
            return 
         elif monthly_income > 100_000_000:
            messagebox.showerror('Invalid Input', "We don't support salaries greater than 100 million")
            return
         elif tax_rate < 0 or tax_rate > 50:
            messagebox.showerror('Invalid Input', 'Make sure your tax rate is valid and within range from 0 to 50')
            return
         
         result_window(monthly_income, tax_rate, current_currency, main_window, monthly_sub_fee, monthly_loan_fee)
         
      except ValueError:
          try:
             monthly_income: float = float(monthly_income1.get())
          except ValueError:
            messagebox.showerror('Invalid Input', 'Make sure your salary is a number')
            return
          try:
             tax_rate: float = float(tax_rate1.get())
          except ValueError:
            messagebox.showerror('Invalid Input', 'Make sure your tax rate is a number')
            return
      
   calc_start = Button(frame2, text='Calculate',  command=checkval)
   calc_start.pack()
   calc_start.config(font=('font', 12))
   
   currency_list : list = ['€','$','£','¥','PLN']
   currency = StringVar(frame2)
   currency.set(currency_list[0])
   Multi_Box = OptionMenu(frame2, currency, *currency_list)
   Multi_Box.pack()
   Multi_Box.config(font=('font', 12))

   guidance = Label(frame3, text='Step-By-Step', bg='darkgrey', font='Arial')
   guidance.pack(pady=[5,0], fill='x')
   guidance.config(font=('Font', 15))
   guidance_description = Label(frame3, text='''
1.Enter your monthly gross amount to the box (It can be real or aproximate).
2.Enter the tax rate to the box based on your state or country.
3.If you want to include optional fees you can add it on the right side.
4.Choose the currency from the list beneath the "Calculate" button.
5.Proceed to calculation by pressing the button "Calculate". 
   ''', bg='darkgrey', font=('Arial', 9) )
   guidance_description.pack(fill='x')
   guidance_description.config(font=('Font', 12))
   
   main_window.mainloop() #   creates visual window


#   This will prevent script from running if executed from another file, will work only if executed in this file

if __name__ ==  '__main__':
    main()