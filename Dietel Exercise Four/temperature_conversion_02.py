def celsius_converter():
        fahrenheit = 0
        result_list = []
        for celsius in range(0, 101):
                fahrenheit = (9 / 5) * celsius + 32
                
                f_string = f"Celsius at {celsius} is: {fahrenheit: .1f} fahrenheit " 
        
        result_list.append(f_string)
        return result_list
                
                
result = celsius_converter()

for item in result:
        print(item)
