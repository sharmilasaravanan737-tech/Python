#loop
#print numbers from 1 to 10
for i in range(1,11,):
  print(i)

  #reverse
for i in range(10,0,-1):
 print(i)

 #even
 for i in range(2,51,2):
   print(i)

#odd
for i in range(1,51,2):
  print(i)

#multiplication
number = int(input("enter number:"))

for i in range(1,11):
   print(number,"x",i,"=",number * i)


 #sum of numbers from 1 to n
n = int(input("enter n:"))

total = 0

for i in range(1,n+1):

  total = total + i
  print("sum:",total)   

#factorial
n = int(input("enter number :"))
factorial = 1

for i in range (1,n + 1):
  factorial = factorial * i
  print("factorial:",factorial)

#sum of even numbers
n = int(input("enter n:"))
total = 0
for i in range(2,n + 1,2):
 total = total + i
 print("sum:",total)

#count of multiple of 3
n = int(input("enter n:"))
count = 0
for i in range(1,n+1):
  if i % 3 == 0 :
    count = count + 1
print("count:",count)

#sum of multiple of 5
n = int(input("enter n :"))
total = 0
for i in range(5,n+1):
  if i % 5 == 0:
    total= total + i
    print("sum:",total)

#even numbers
i = 2

while i<=50 :
  print(i)
  i = i + 2

#odd numbers
i = 1
while i<=50:
  print(i)
  i = i + 2

#print total numbers printed by users until 0 is entered
total = 0
number = int(input("enter number :"))

while number !=0:
  total = total + number 
  number = int(input("enter number:"))

  print("total:",total)

#password check 
password = ""
while password != "python123":
  password = input("enter password:")

  print("Login successful")

#count the number of digits in a Number
number = int(input("enter number:"))

count = 0

while number > 0:
   number = number // 10
   count = count + 1

   print("Number of digits:",count)

#sum of digits in a number
number = int(input("Enter number: "))

total = 0

while number > 0 :
  digit = number % 10
  number = number // 10
  total = total + digit

print("sum of digits:",total)

#Reverse a number
number = int(input("Enter number:"))

reverse = 0
while number >0:
  digit = number % 10
  number = number // 10
  reverse = reverse * 10 + digit

print("Reverse :",reverse)  

#Palindrome
number = int(input("Enter number: "))
original = number
reverse = 0

while number >0:
  digit = number % 10
  number = number // 10
  reverse = reverse * 10 + digit

if original == reverse:
  print("Palindrome")
else:
     ("Not Palindrome")

#check if a number is prime
number = int(input("Enter number:"))

count = 0

for i in range(1,number + 1):
  if number % i   == 0 :
    count = count + 1

if count == 2:
 print("prime number")
else:
  print("Not a prime number")

#print all number between 2 to  100
for number in range(2,101):

  count = 0
for i  in range (1,number + 1):
  if number % i == 0 :
    count = count + 1

if count == 2:
  print(number)

#break
for i in range(1,11):
  if i == 5:
    break #exit the loop
  print(i)


#continue
for i in range(1,11):
  if i == 4:
    continue #skip th current iteration and continue the next loop

  print(i)


#pass
for i in range(1,10):
  if i == 3:
    pass
  print(i)


#break
for i in range(1,11):
  if i ==7 :
    print("Number Found")
    break
  print(i)

#print odd numbers from 1 to 10
for i in range(1,11):
  if i % 2 == 0:
   continue

  print(i)

#print even numbers 1 to 10
for i in range(1,11):
  if i % 2 == 0:
   continue
  print(i)

#print numbers until user enters 0
while True:

  number = int(input("Enter number :"))

  if number == 0:
    break
  print("You entered :",number)

#print numbers 1 to 100 , but skip multiples of 3 and stop at 50
for i in range(1,101):

  if i == 50:
    break
  if i % 3 == 0:
    continue
  print(i)

#calculate the sum of positive numbers
total = 0
while True:
  number = int(input("Enter Number:"))

  if number < 0 :
    continue

  if number == 0:
    break

  total = total + number

  print("Total number:",total)  

  #find the first number between 1 and 100 that  is divisible 3 and 5
  for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
      print("First number:",i)
      break


#calculate the sum of positive numbers entered by the users
total = 0
for i in range(10):
  number = int(input("enter number:"))

  if number < 0:
    continue

  total = total + number

#password check
correct_password = "python123"

for attempt in range(1,4):
  password = input("enter password :")

  if password == correct_password:
    print("login Successful")
    break
  print("Wrong password")

else:
  print("account locked")

#findthe largest number among 5 numbers entered by the user
largest = None

for i in range(5):

  number = int(input("Enter number:"))

  if largest is None or number > largest :
    largest = number

print("largest:",largest)

#find the smallest number among 5 numbers entered by the user
smallest = None

for i in range(5):

  number = int(input("Enter number:"))

  if smallest is None or number < smallest :  
    smallest = number

print("Smallest:",smallest)

#






