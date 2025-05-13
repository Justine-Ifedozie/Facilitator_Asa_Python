"""World Population Growth"""
#Calculate world population each year for the next 100 years. Growth rate will stay constant.

current_world_population = float(input("Enter the present world population: "))

growth_rate_per_year = float(input("Enter the population yearly growth rate: "))

population_growth_rate_per_year = growth_rate_per_year / 100

print('Years\t Anticipated World Population\t Numerical increase yearly\t')

for  counter in range (1, 101):
    print(counter)
    #first_world_population = current_world_population * ((1 + population_growth_rate_per_year) ** counter)
    #print(counter, "\t", first_world_population, "\t")
 