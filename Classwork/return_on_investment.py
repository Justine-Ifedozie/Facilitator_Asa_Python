#Return for an investment

investment_amount = float(input("Enter investment_amount: "))
number_of_years = int(input("Enter number of years: "))
interest_rate = float(input("Enter interest rate: "))
interest_rate_1 = interest_rate / 100
years_count = 1
for years_count in range (1, number_of_years):
     first_year = investment_amount * interest_rate_1 * years_count
     sum = first_year + investment_amount
     print(f'Your return on investment for year {years_count} is: ${sum: ,.2f}')
     
     
             #print(f'Your discount is: ${discount: ,.2f}')