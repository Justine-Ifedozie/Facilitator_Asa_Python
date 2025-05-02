#Mortgage Calculator

#Prompt the client for the amount he wishes to borrow (P - Principal amount).
#Prompt the client for the annual interest rate offered on the mortgage (r - rate).
	#To get r divide annual interest rate by percentage (100) then divide the result by a constant (12 months in a year). 
#Prompt the client for the duration of the mortgage in years (n - the duration of the loan).
	#Multiply it by 12(number of months in a year).

#Automatically calculate the monthly payment for the client (Apply the given formula).
	#1 plus r then raise to power the result by n. Then multiply what you get with r to find the Numerator.
	#1 plus r then raise to power the result by n, then deduct 1. Denominator.
	#Divide the numerator by the denominator.
	#Muliply the result by p to find M.
#Display the monthly payment.

#Where,
#p = principalAmount
#r = rate
#n = mortgageDuration

#m = numberOfMonths

principal_amount = int (input("Enter the principal amount: "))

annual_interest = float (input("Enter the annual interest rate: "))

duration_of_mortgage = float (input("Enter the duration of the mortgage in years: "))

#Calculation for rate (r).
rate = annual_interest / 100 / 12

#Calculate for loan duration (n)
loan_duration = duration_of_mortgage * 12

#Calculation for the monthly payment
numerator_1 = 1 + rate
numerator_2 = numerator_1 ** loan_duration
numerator = rate * numerator_2 

denominator_1 = 1 + rate
denominator_2 = denominator_1 ** loan_duration
denominator = denominator_2 - 1

fraction_result = numerator / denominator
monthly_payment = principal_amount * fraction_result

#Round up the answer to 2 decimal places.
rounded_monthly_payment = round (monthly_payment, 2)

#Display the result
#print("Your monthly payment is: $")
#print(rounded_monthly_payment)

print(f" Your monthly payment is:  {rounded_monthly_payment}")

