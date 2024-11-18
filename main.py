from modules import *
from other_modules import result_window

#   Begining of TKinter Window  #
def main() -> None:

   main_window = tk.Tk()
   main_window.title('Financial Calculator')

   win_h = 400
   win_w = 520
   screen_w = main_window.winfo_screenwidth()
   screen_h = main_window.winfo_screenheight()

   x_cord = int((screen_w/2) - (win_w/2))
   y_cord = int((screen_h/2) - (win_h/2))

   main_window.geometry("{}x{}+{}+{}".format(win_w, win_h, x_cord, y_cord))

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

   monthly_income1 = Entry(frame2, width=25, justify='center')
   monthly_income1.insert(0, 'Enter your monthly salary')
   monthly_income1.bind("<FocusIn>", on_entry_click1)
   monthly_income1.bind("<FocusOut>", on_focus_out1)
   monthly_income1.pack(pady=[10,0])

   tax_rate1 = Entry(frame2, width=25, justify='center')
   tax_rate1.insert(0, 'Enter your tax rate')
   tax_rate1.bind("<FocusIn>", on_entry_click2)
   tax_rate1.bind("<FocusOut>", on_focus_out2)
   tax_rate1.pack(pady=[0,10])
   
   def checkval() -> None:
      try:
         monthly_income: float = float(monthly_income1.get())
         tax_rate: float = float(tax_rate1.get())
         current_currency: str = currency.get()
         if monthly_income < 100:
            messagebox.showerror('Invalid Input', 'Make sure your salary is valid and above 100')
            return None
         elif tax_rate < 0:
            messagebox.showerror('Invalid Input','Make sure your tax rate is valid and within range from 0 to 50')
            return None
         elif tax_rate > 50:
            messagebox.showerror('Invalid Input','Make sure your tax rate is valid and within range from 0 to 50')
            return None
      except ValueError:
         if tax_rate == None or monthly_income == None:
            messagebox.showerror('Data type error', 'Use numbers only!')
            return None
         if type(tax_rate) != int or type(tax_rate) != float:
            messagebox.showerror('Data type error', 'Please enter numbers only in tax rate box!')
            return None
         elif type(monthly_income) != int or type(monthly_income) != float:
            messagebox.showerror('Data type error', 'Please enter numbers only in income box!')
      else:
         result_window(monthly_income1, tax_rate1, currency, main_window)

   calc_start = Button(frame2, text='Take me to the Calculator',  command=checkval)
   calc_start.pack()
   calc_start.config(font=('font', 10))
   
   currency_list : list = ['€','$','£','¥','zł']
   currency = StringVar(frame2)
   currency.set(currency_list[0])
   Multi_Box = OptionMenu(frame2, currency, *currency_list)
   Multi_Box.pack()

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


#   This will prevent script from running if executed from another file, will work only if executed in this file

if __name__ ==  '__main__':
    main()