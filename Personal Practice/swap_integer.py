#Swap two integers without using a temporary variable

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))

a = a + b
b = a - b
a = a - b

print(a, b)