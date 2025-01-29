from modules import *
from other_modules import result_window

#   Begining of TKinter Window  #
def main() -> None:

   main_window = tk.Tk()
   main_window.title('Financial Calculator')

   win_h = 720
   win_w = 1080
   screen_w = main_window.winfo_screenwidth()
   screen_h = main_window.winfo_screenheight()

   x_cord = int((screen_w/2) - (win_w/2))
   y_cord = int((screen_h/2) - (win_h/2))

   main_window.geometry("{}x{}+{}+{}".format(win_w, win_h, x_cord, y_cord))

   main_window.resizable(False,False)

   frame1 = Frame(main_window,relief=RAISED, name='header')
   frame1.pack(fill='x')
   frame3 = Frame(main_window,relief=RAISED, name='description')
   frame3.pack(fill='x', side='top')
   frame2 = Frame(main_window,relief=RAISED, name='body-left')
   frame2.pack(side='left', padx=120, fill='both')
   frame4 = Frame(main_window,relief=RAISED, name='body-right')
   frame4.pack(side='left', padx=120, fill='both')

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
      if monthly_sub_fee1.get() == 'Enter your monthly subscription fee':
         monthly_sub_fee1.delete(0, tk.END)
         monthly_sub_fee1.configure(foreground="black")
   def on_focus_out3(event):
      if monthly_sub_fee1.get() == "":
         monthly_sub_fee1.insert(0, 'Enter your monthly subscription fee')
         monthly_sub_fee1.configure(foreground="gray")
   
   def on_entry_click4(event):
      if monthly_loan_fee1.get() == 'Enter your monthly loan fee':
         monthly_loan_fee1.delete(0, tk.END)
         monthly_loan_fee1.configure(foreground="black")
   def on_focus_out4(event):
      if monthly_loan_fee1.get() == "":
         monthly_loan_fee1.insert(0, 'Enter your monthly loan fee')
         monthly_loan_fee1.configure(foreground="gray")

   title = Label(frame1, text='Welcome to the Calculator', bg='lightblue')
   title.pack(fill='x')
   title.config(font=('Font', 35))

   monthly_income1 = Entry(frame2, width=25, justify='center')
   monthly_income1.insert(0, 'Enter your monthly salary')
   monthly_income1.bind("<FocusIn>", on_entry_click1)
   monthly_income1.bind("<FocusOut>", on_focus_out1)
   monthly_income1.pack(pady=[10,0])
   monthly_income1.config(font=('Font', 15), justify='center')

   tax_rate1 = Entry(frame2, width=25, justify='center')
   tax_rate1.insert(0, 'Enter your tax rate')
   tax_rate1.bind("<FocusIn>", on_entry_click2)
   tax_rate1.bind("<FocusOut>", on_focus_out2)
   tax_rate1.pack(pady=[0,10])
   tax_rate1.config(font=('Font', 15))

   monthly_sub_fee1 = Entry(frame4, width=25, justify='center')
   monthly_sub_fee1.insert(0, 'Enter your monthly subscription fee')
   monthly_sub_fee1.bind("<FocusIn>", on_entry_click3)
   monthly_sub_fee1.bind("<FocusOut>", on_focus_out3)
   monthly_sub_fee1.pack(pady=[10,0])
   monthly_sub_fee1.config(font=('Font', 15))

   monthly_loan_fee1 = Entry(frame4, width=25, justify='center')
   monthly_loan_fee1.insert(0, 'Enter your monthly loan fee')
   monthly_loan_fee1.bind("<FocusIn>", on_entry_click4)
   monthly_loan_fee1.bind("<FocusOut>", on_focus_out4)
   monthly_loan_fee1.pack(pady=[0,10])
   monthly_loan_fee1.config(font=('Font', 15))
   
   def checkval() -> None:
      try:
         monthly_income: float = float(monthly_income1.get())
         tax_rate: float = float(tax_rate1.get())
         current_currency: str = currency.get()
         monthly_sub_fee: float = float(monthly_sub_fee1.get())
         monthly_loan_fee: float = float(monthly_loan_fee1.get())
         
         if monthly_income < 100:
            messagebox.showerror('Invalid Input', 'Make sure your salary is valid or above 100')
            return
         elif monthly_income > 100_000_000:
            messagebox.showerror('Invalid Input', "We don't support salaries greater than 100 million")
            return
         elif tax_rate < 0 or tax_rate > 50:
            messagebox.showerror('Invalid Input', 'Make sure your tax rate is valid and within range from 0 to 50')
            return
         
      except ValueError:
         messagebox.showerror('Data type error', 'Please enter valid numbers in the input boxes!')
         return None
      
      result_window(monthly_income, tax_rate, current_currency, main_window, monthly_sub_fee, monthly_loan_fee)
   calc_start = Button(frame2, text='Take me to the Calculator',  command=checkval)
   calc_start.pack()
   calc_start.config(font=('font', 12))
   
   currency_list : list = ['€','$','£','¥','PLN']
   currency = StringVar(frame2)
   currency.set(currency_list[0])
   Multi_Box = OptionMenu(frame2, currency, *currency_list)
   Multi_Box.pack()
   Multi_Box.config(font=('font', 12))

   guidance = Label(frame3, text='Introduction', bg='darkgrey', font='Arial')
   guidance.pack(pady=[10,0], fill='x')
   guidance.config(font=('Font', 15))
   guidance_description = Label(frame3, text='''
   1. In box with Monthly Salary please enter real or aproximate value to yor earning.
   2. In box with tax rate enter a number before the '%' corresponding with your state or country.
   3. After filling above boxes procced to calculation.
   ''', bg='darkgrey', font=('font', 9) )
   guidance_description.pack(fill='x')
   guidance_description.config(font=('Font', 12))
   
   main_window.eval('tk::PlaceWindow . center')
   main_window.mainloop() #   creates visual window


#   This will prevent script from running if executed from another file, will work only if executed in this file

if __name__ ==  '__main__':
    main()