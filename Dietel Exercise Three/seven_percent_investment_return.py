#Exercise_3.10
invested_amount_p = 1000
annual_rate_of_return_r = 7/100
result = 0

for count in range(1, 31):
    amount_of_deposit_end_ten = invested_amount_p * ((1 + annual_rate_of_return_r) ** count)
    result = round(amount_of_deposit_end_ten, 2)
    print(f"Money you'll have after {count} years is: $ {result: ,.2f}")