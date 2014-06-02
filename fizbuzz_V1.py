import sys

while len(sys.argv) <= 1:
	number = raw_input("Enter any number: ")
	number = int(number)
	if number % 3 == 0 and number % 5 == 0:
		print "FizzBuzz"
	elif number % 3 == 0:
		print "Fizz"
	elif number % 5 == 0:
		print "Buzz"
	else:
		print number
else:
	for num in sys.argv[1:]:
		if int(num) % 3 == 0 and int(num) % 5 == 0:
			print "FizzBuzz"
		elif int(num) % 3 == 0:
			print "Fizz"
		elif int(num) % 5 == 0:
			print "Buzz"
		else:
			print num
		
