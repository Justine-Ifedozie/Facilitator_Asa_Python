
item_purchase_price = float(input("Input purchase price: "))

amount_paid = float(input("Amount paid: "))

cents = item_purchase_price - amount_paid

print("Your change is: ")
print(cents, "cents")


quarters = cents// 25
change1 = quarters % 25
print(change1, "quarters")

dimes = cents // 10
change2 = dimes % 10
print(change2, "dimes")

pennies = cents % 1
print(cents, "pennies")
