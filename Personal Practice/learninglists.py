list = [10, 20, 30, 40, 50]
for index in range(len(list)):
        print(list[index])


characters = []
characters += 'Birthday'
print(characters)
print(characters[3])

student_tuple = ('John', 'Green', 3.2)
student_tuple2 = ('Justine', 'Red', 3)
student_tuple2 += (1, 2)
len(student_tuple)
print(student_tuple, student_tuple2)

list = student_tuple
print(list[1])


grade_tuple = ('Amanda', 'Blue', [98, 85])
print(grade_tuple[2][0])

first, second = 'hi'
print(f'{first} {second}')

#Swapping values through packing and unpacking
number1 = 99
number2 = 22
number1, number2 = (number2, number1)
print(f'number1 = {number1}; number2 = {number2}')


colours = ['red', 'orange', 'yellow', 'green']
#list(enumerate(colours))
#print(list)
tuple(enumerate(colours))
for index, value in enumerate(colours):
        print(f' {index} {value}')

#Practicing sequence slicing
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(numbers[1:5])

del numbers[0:3]
print(numbers)






