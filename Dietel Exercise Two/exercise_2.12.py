#Exercise_2.12

invested_amount_p = 1000

annual_rate_of_return_r = 7 / 100

number_of_years_ten = 10
number_of_years_twenty = 20
number_of_years_thirty = 30

amount_of_deposit_end_ten = invested_amount_p * ((1 + annual_rate_of_return_r) ** number_of_years_ten)
result_1 = round(amount_of_deposit_end_ten, 2)

amount_of_deposit_end_twenty = invested_amount_p * ((1 + annual_rate_of_return_r) ** number_of_years_twenty)
result_2 = round(amount_of_deposit_end_twenty, 2)

amount_of_deposit_end_thirty = invested_amount_p * ((1 + annual_rate_of_return_r) ** number_of_years_thirty)
result_3 = round(amount_of_deposit_end_thirty, 2)

print("Money you'll have after 10 years is: $", result_1)

print("Money you'll have after 20 years is: $", result_2)

print("Money you'll have after 30 years is: $", result_3)