#Declare the three discounts in percentage (Constants)
        #Calculate each discounts by dividing it by 100 to get the floating point value
        
#Receive inputs 



five_percent = 5 / 100
ten_percent = 10/ 100
twenty_percent = 20/ 100

purchase_amount = int(input('Enter purchase amount: '))

if purchase_amount >= 1000 and purchase_amount <= 10000:
        discount = purchase_amount * five_percent
        price = purchase_amount - discount
        print(f'Your discount is: ${discount: ,.2f}')
        print(f"You're to pay: $price")
        
elif purchase_amount > 10000 and purchase_amount < 50000:
        discount = purchase_amount * ten_percent
        price = purchase_amount - discount
        print(f'Your discount is: ${discount: ,.2f}')
        print("You're to pay:", price)


elif purchase_amount > 50000:
        discount = purchase_amount * twenty_percent
        price = purchase_amount - discount
        print(f'Your discount is: ${discount: ,.2f}')
        print("You're to pay:", price)

        
else: 
        print("Invalid input")
