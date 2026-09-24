#comparison operator
a = 10
b = 20
print(a == b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#age eligibility
age  = int(input("enter your age:"))

print("eligible:", age>=18)

#pass or fail
marks = int(input("enter your marks:"))

print("Passed:",marks>=40)

#login validation
correct_username = "admin"
correct_password = "1234"

username = input("enter username:", )
password = input("enter password:", )

print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True

print(age>=18 and citizen == True)

age = 16
citizen = True

print(age>=18 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash )

is_logged_in = True

print(not is_logged_in)

#Atm  eligibility checker
balance = 10000
withdraw = 2000

print(withdraw > 0 and withdraw <= balance)

#student Scholarship eligibility checker
marks = float(input("enter marks:" ))
attendance = float(input("enter attendance:", ))

eligible = marks >= 85 and attendance >=75

print("scholarship eligible:", eligible)

#identity operators

a = None

print(a is None)
print(a is  not None)

#bitwise operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(a << b) 
print(a >> b)

#electric city bill calculator

units = int(input("enter electricity units:"))

rate = 6
bill = units * rate
print("Electricity Bill:", bill)


#Travel Expense Calculator
travel = float(input("travel expense:"))
food = float(input("food expense:"))
hotel = float(input("Hotel expense: "))


total  = travel + food + hotel
print("Total Expense :",total)

#list in python
#list is an Ordered and changeable collection that can store and it is mutable
marks = [80,90,85,75]

print(marks)

#acessing elements in a list
marks = [80,90,87,89]

print(marks[0])
print(marks[1])
print(marks[2])

#change elements in a list
marks = [80,90,88]

marks[1] = 95

print(marks)

#add elements  to a list
marks = [80,90,89]

marks.append(85)

print(marks)

# remove elements from the list 
marks = [80,90,66]

marks.remove(66)

print(marks)

#list of numbers
numbers = [10,20,30]

numbers.insert(1,15,)
numbers.insert(2,25)

print(numbers)

#extend
a = [1,2,3,4]
b = [5,6,7,8]

a.extend(b)

print(a)

#clear
numbers = [10,20,30,40]

numbers.clear()

print(numbers)

#index
numbers  = [10,20,30,40,50,60,70,80,90]

print(numbers.index(90))

#count
numbers = [10,20,40,40,55,30,20,10]
print(numbers.count(40))

#sort 
numbers = [10,20,30,40,50]

numbers.sort()

print(numbers)

numbers.sort(reverse = True)

print(numbers)

#reverse
numbers = [10,20,30,40]

numbers.reverse()
print(numbers)

#copy
a = [1,2,3,4]

b = a.copy()

print(b)

#slicing
#start:stop:step
numbers = [10,20,30,40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:: -1])

#Tuples in python 
#Tuple is a collection of multiple values that is ordered and not changeable after creation and is immutable
student = ("Sharmila ",98,"python")
print(student[0])

#access values in a tuple
student =("Bhargavi",21,85.5)

print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples
numbers = (10,20,30,20,30)

print(numbers.count(20))

#index
numbers = (10,20,30,40,50)
print(numbers.index(30))

#length
numbers = (10,20,30,40,50)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable.
numbers = {10,20,30,30,20}

print(numbers)

#why use set
#suppose students have selected subjects
subjects = {"python","java","sql","python","java"}
print(subjects)

#add values in set
subjects = {"python","java"}

subjects.add("sql")
print(subjects)

#remove values in set
subjects = {"python","java"}
subjects.remove("java")
print(subjects)

#set do not allow duplicate values
numbers = {1,2,3,4,5,3}

print(numbers)

#slicing
numbers = [10,20,30,40,50,60,70,80]

print(numbers[1:7:2])
print(numbers[6:1:-2])

total_number = int(input("enter number:", ))
Hours = 1
min = 60
Seconds = 36
print(Hours)
print(min)
print(Seconds)


