"""World Population Growth"""
#Calculate world population each year for the next 100 years. Growth rate will stay constant.

present_world_population = float(8005176000)

growth_rate_per_year = float(0.85)

population_growth_rate_per_year = growth_rate_per_year / 100

double_population = 0

quadruple_population = 0

print('Years\t\t Anticipated World Population\t\t Numerical increase yearly\t')

for  counter in range (1, 101):
        previous_world_population = present_world_population
        
        present_world_population = previous_world_population * (1 + population_growth_rate_per_year)
        
        numerical_increase = present_world_population - previous_world_population
        
        print(f"Year {counter}. \t\t- {previous_world_population:,.2f} \t\t- {numerical_increase:,.2f}")
        
#Determining the year that the population is double and eventually quadraple what it is today
        if double_population == 0 and present_world_population >= previous_world_population * 2:
                double_population = counter
                
        if quadruple_population == 0 and present_world_population >= previous_world_population * 4:
                quadruple_population = counter

if double_population != 0:
        print(double_population)
else:
        print("There was no double population within 100 years")
        
if quadruple_population != 0:
        print(quadruple_population)
else:
        print("There was no quadruple population within 100 years")
        
        
