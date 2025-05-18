#exercise_3.21

one_dollar_purchase_price = float(input("Enter purchase price (in cents = 100 cents): "))
cost_of_product = float(input("Enter cost of product (27 cents): "))

change = one_dollar_purchase_price - cost_of_product
print(f'Your change is: {change} cents')

quarters = change // 25
print(f'Your change is: {quarters} quarters')
change = change % 25

dimes = change // 10
print(f'Your change is: {dimes} dimes')
change = change % 10

nickels = change // 5

pennies = change % 5
print(f'Your change is: {pennies} pennies')