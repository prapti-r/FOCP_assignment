#input a number
number = input("Enter a number: ")

#convert the input to an integer
number = int(number)

#print the entered number
print("The numbered entered was", number)

#check if the number is even or odd
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")

#check if the number is divisible by 10
if (number % 10) == 0:
    print("The number is divisible by 10")
else:
    print("The number is not divisible by 10")