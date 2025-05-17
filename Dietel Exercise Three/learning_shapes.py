#Learning shapes printing.

n = 8
for count in range(n):
    for counter in range(count+1):
        print('*', end = " ")
    print()
    
print("\n")  
  
  
for count in range(n):
    for counter in range(count, n):
        print('*', end = " ")
    print()
    
print("\n")  

for counter in range(n):
    for count in range(counter , n):
        print(' ', end = ' ')
    for count in range(counter + 1):
        print('*', end = " ")
    print()
        
print() 
        
for counter in range(n):
    for count in range(counter +1):
        print(' ', end = " ")
    for count in range(counter, n):
        print('*', end = " ")    
    
    print()