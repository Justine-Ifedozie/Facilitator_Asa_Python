payroll = []

def add_employee_payroll(hours_worked, hourly_pay_rate):
        gross_pay = hours_worked * hourly_pay_rate
        return gross_pay
        
def federal_witholding(federal, federalTaxRate):
        federal_with = (federalTaxRate / 100) * federal
        return federal_with

def state_witholding(state, stateTaxRate):
        state_with = (stateTaxRate / 100) * state
        return state_with

def total_deduction(federal, state):
        total = federal + state
        return total

def net_pay(gross_pay, total):
        net = gross_pay - total
        return net

