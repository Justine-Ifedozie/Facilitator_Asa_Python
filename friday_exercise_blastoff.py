#Today's assignment

n = int(input("Enter an integer:  "))
for values in range(n, 0, -1):
    print(values)
    if values == 1:
        print("Blast Off!")
    elif values < 1:
        n = (input("Enter an integer:  "))
