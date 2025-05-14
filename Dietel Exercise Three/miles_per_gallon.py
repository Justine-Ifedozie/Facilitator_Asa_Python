#Miles Per Gallon

gallons_used = 0
miles_driven = 0
miles_per_gallon_tank = 0
average = 0
total_miles_driven = 0
total_gallons_used = 0

while gallons_used != -1:
    gallons_used = float(input("Enter the gallons used (-1 to end): "))
    
    if gallons_used != -1:
        miles_driven = float(input("Enter the miles driven: "))
        total_miles_driven  += miles_driven
        miles_per_gallon_tank = miles_driven / gallons_used
        total_gallons_used += gallons_used
        
        print("The miles/ gallon for this tank was: ", miles_per_gallon_tank)
        average = total_miles_driven / total_gallons_used
        
print("The overall average miles/ gallon was: ", average)