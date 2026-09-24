#basic Function 
def greet():
    print("Hello World")
    print("Welcome to python")

greet()

#Functions without Parameters
def welcome():
    print ("welcome to python")

welcome()
welcome()
welcome()

#Function with parameters
def greet(name):
    print("Hello",name)

greet("Bhargavi")
greet("Nymi")
greet("Sharmi")

#Multiple parameters
def add(a,b):
    print("Sum :",a + b)
add(10,20)
add(50,30)

#function with return value
def add(a,b):
    return a + b                             #returns the value to the result and that result send to parameter and performs the task

result = add(10,20)

print(result)      

#Return
def  add(a,b):
    return a + b
result = add(10,20)
if result > 25 :
    print("Larger Number")

#Functions for even/odd numbers
def check_even_odd(number):

    if number % 2 == 0 :
        return "even"
    else:
        return "Odd"

result = check_even_odd(25)
print(result)

#print largest of two numbers
def largest(a,b):

    if a > b :
        return a
    else:
        return b
result = largest(22,15)
print("largest:",result)

#print largest of three numbers
def largest(a,b,c):
    if a > b :
        return a
    
    if b > c :
        return b 

    if a > c :
        return a
    
    
