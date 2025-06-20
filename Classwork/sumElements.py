import random
number_one = random.randint(1,50)
number_two = random.randint(1,50)
number_three = random.randint(1,50)
number_four = random.randint(1,50)
number_five = random.randint(1,50)
number_six = random.randint(1,50)
number_seven = random.randint(1,50)
number_eight = random.randint(1,50)
number_nine = random.randint(1,50)
number_ten = random.randint(1,50)

list = [number_one, number_two, number_three, number_four, number_five, number_six, number_seven, number_eight, number_nine, number_ten]

print(list)

def sumEvenElements(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    print("Sum of even elements in the list is: ", sum)

sumEvenElements(list)

def sumOddElements(list):
    sum = 0
    for i in list:
        if i % 2 == 1:
            sum += i
    print("Sum of odd elements in the list is: ", sum)

sumOddElements(list)

def multiplyAllElementsAtThirdPositions(list):
    multiplied_result = 0
    for i in list:
        if i % 3 == 0:
            multiplied_result += i
    print("Multiplication of all elements in the third position: ", multiplied_result)

multiplyAllElementsAtThirdPositions(list)

def calculateAverage(list):
    average = 0
    sum = 0
    for i in list:
        sum += i
        average = sum / 10
    print("Average of even elements in the list is: ", average)

calculateAverage(list)