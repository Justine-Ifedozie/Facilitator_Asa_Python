#Find the highest score

student_number = int(input("Enter students number: "))

counter = 0
student_score = 0
high_score = student_score
student_name = " "
high_name = student_name
grade_counter = 0
sentinel_value = 0
    
while sentinel_value != -1:
    student_name =  str(input("Enter students name: "))
    student_score = int(input("Enter students score: "))
    
    sentinel_value = int(input("Enter -1 to end the game or any number to continue: "))

    
    if student_score > high_score and student_score != -1:
        high_score = student_score
        high_name = student_name
    grade_counter += 1

print(high_name, " has the highest score of: ", high_score)
