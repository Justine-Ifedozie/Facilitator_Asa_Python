import random

count = 1
counter = 0

while count != 10:
	computer_guess = random.randrange(1, 100)

	computer_guess_two = random.randrange(1, 100)

	temp = 0
	result = 0

	if minuend > subtrahend:
		minuend = subtrahend

	else:
		temp = minuend
		minuend = subtrahend
		subtrahend = temp

	result = minuend - subtrahend;
	print(result);
	userAnswer = int(input("What is the answer to: " + minuend + " - " + subtrahend + ": ")

	if result == userAnswer:
		print("You got the right answer")
		counter++

	else
		print("Wrong answer! you have one trial");
		print("What is the answer to: " + minuend + " - " + subtrahend + ": ");
		userAnswer = int(input("What is the answer to: " + minuend + " - " + subtrahend + ": ")

	count++


print("Your score is " + counter + " out of " + count + " questions")


