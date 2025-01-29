def calculate_finances(monthly_income1: float, tax_rate1: float, currency: str, monthly_sub_fee:int, monthly_loan_fee: int) -> float:
    
    monthly_tax: float = monthly_income1 * (tax_rate1 / 100)
    monthly_net_income: float = monthly_income1 - monthly_tax
    monthly_sub_loan_fee = monthly_sub_fee + monthly_loan_fee
    monthly_net_income_m_fee = monthly_net_income - monthly_sub_loan_fee

    yearly_salary: float = monthly_income1 * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_sub_loan_fee = monthly_sub_loan_fee * 12
    yearly_net_income_m_fee = yearly_net_income - yearly_sub_loan_fee




#   |,.2f| Will round the number to two places after point

    MI = (f'Montly income: {currency} {monthly_income1: ,.2f}')
    TR = (f'Tax rate: {tax_rate1:,.0f}%')
    MT = (f'Monthly tax: {currency} {monthly_tax:,.2f}')
    MNI = (f'Monthly net income: {currency} {monthly_net_income:,.2f}')
    MF = (f'Monthly fees: {currency} {monthly_sub_loan_fee:,.2f}')
    MNIF = (f'Monthly net income minus fees: {currency} {monthly_net_income_m_fee:,.2f}')
    YS = (f'Yearly salary: {currency} {yearly_salary:,.2f}')
    YTP = (f'Yearly tax to pay: {currency} {yearly_tax:,.2f}')
    YNI = (f'Yearly net income: {currency} {yearly_net_income:,.2f}')
    YF = (f'Yearly fees: {currency} {yearly_sub_loan_fee:,.2f}')
    YNIF = (f'Yearly net income minus fees: {currency} {yearly_net_income_m_fee:,.2f}')
    print('Output has been sent')
    
    return MI, TR, MT, MNI, MF, MNIF, YS, YTP, YNI, YF, YNIF