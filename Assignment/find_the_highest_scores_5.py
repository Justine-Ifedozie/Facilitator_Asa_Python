#Find the highest score. 5.9

student_number = int(input("Enter students number: "))

counter = 0
student_score = 0
high_score = student_score
second_highest_score = high_score
second_highest_name = " "
student_name = " "
high_name = student_name
grade_counter = 0
sentinel_value = 0
    
for count in range(0, student_score):
    student_name =  str(input("Enter students name: "))
    student_score = int(input("Enter students score: "))
    
    sentinel_value = int(input("Enter -1 to end the game or any number to continue: "))

    
    if student_score > high_score:
       # second_highest_score = high_score
        high_score = student_score
        high_name = student_name
    grade_counter += 1
    
    if second_highest_score > high_score:
        high_score = second_highest_score
        second_highest_score = student_score

print(high_name, " has the highest score of: ", high_score)
print(second_highest_name, " has the second highest score of: ", second_highest_score)
