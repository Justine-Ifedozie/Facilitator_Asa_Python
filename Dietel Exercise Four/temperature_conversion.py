def celsius_converter():
        fahrenheit = 0
        for celsius in range(0, 101):
                fahrenheit = (9 / 5) * celsius + 32
                print(f"Celsius at {celsius} is: {fahrenheit: .1f} ")
        return 
                
                
result = celsius_converter()
print(result)