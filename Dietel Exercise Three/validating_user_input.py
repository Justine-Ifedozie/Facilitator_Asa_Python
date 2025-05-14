# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
	result = int(input('Enter result (1=pass, 2=fail): '))
	result = int(input('Enter result (1=pass, 2=fail): '))

	if result == 1:
		passes = passes + 1
	else:
		failures = failures + 1