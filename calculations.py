def calculate_finances(monthly_income1: float, tax_rate1: float, currency: str) -> float:
    
    monthly_tax: float = monthly_income1 * (tax_rate1 / 100)
    monthly_net_income: float = monthly_income1 - monthly_tax
    yearly_salary: float = monthly_income1 * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

#   |,.2f| Will round the number to two places after point

    text1 = (f'Montly income: {currency} {monthly_income1: ,.2f}')
    text2 = (f'Tax rate: {tax_rate1:,.0f}%')
    text3 = (f'Monthly tax: {currency} {monthly_tax:,.2f}')
    text4 = (f'Monthly net income: {currency} {monthly_net_income:,.2f}')
    text5 = (f'Yearly salary: {currency} {yearly_salary:,.2f}')
    text6 = (f'Yearly tax to pay: {currency} {yearly_tax:,.2f}')
    text7 = (f'Yearly net income: {currency} {yearly_net_income:,.2f}')
    print('Output has been sent')
    
    return text1, text2, text3, text4, text5, text6, text7