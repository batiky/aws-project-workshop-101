#Check if a number is prime or not

# Input taking from user to validate if 
number = 0
while number == 0:
    try:
     number = int(input("Enter the number you want to check: "))     
    except ValueError:
        print("Entered value is not a valid digit type of int!")
    continue
# first conditon to check if input > 1
if  number > 1:
   # actual validationif it is prime
   for digit in range(2,number):
       if (number % digit) == 0:
           print(number,"is not a prime number")
           break
   else:
       print(number,"is a prime number")
         
    # last condition for the input <= 1
else:
    print(number,"is not a prime number")
