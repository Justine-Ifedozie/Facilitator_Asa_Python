#Find the highest score. 5.9

student_number = int(input("Enter students number: "))

counter = 0
student_score = 0
high_score = 0
high_name = " "
second_highest_score = 0
second_highest_name = " "
student_name = " "
sentinel_value = 0
    
for count in range(0, student_number):
    student_name =  str(input("Enter students name: "))
    student_score = int(input("Enter students score: "))
    
    sentinel_value = int(input("Enter -1 to end the game or any number to continue: "))
    if student_score > high_score:
        second_highest_score = high_score
        second_highest_name = high_name
        high_score = student_score
        high_name = student_name
    
    elif student_score > second_highest_score  and student_score != high_score:
        second_highest_score = student_score

print(high_name, " has the highest score of: ", high_score)
print(second_highest_name, " has the second highest score of: ", second_highest_score)
