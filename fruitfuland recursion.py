#default parameteric function
def add(a=10,b=20):
    print(a+b)
add()    

#ordered parametric functions
def add(a,b):
    print(a)
    print(b)
add(10,20)

def add(b,a):
    print(a)
    print(b)
add(10,20)

#keyword arguement parametric function
def add(a,b):
    print(a)
    print(b)
add(a =10,b =20)

def add(a,b):
    print(a)
    print(b)
add(b =20,a =10)

#variable length parametric function
def add(*a):
    print(sum(a))
add(5,6,7,8,9) 

#variable length keyword parameteric function

#anonymous functions or lambda functions 
#syntax:vn = lamda , variables : expressions  
total = lambda a,b,c : a+b+c
print(total(10,20,30))

total  = lambda a : a*a
print(total(5))

#Armstrong number
num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


#map function
# syntax : map(lambda function,iteratable variable)
a = [1,2,3,4]
n = list(map(lambda x : x**2,a))
print(n)

#filter
# syntax : filter(lambda function,iteratable function)
a = [1,2,3,4]
n = list(filter(lambda x :x % 2 == 0,a))
print(n) 

#fruitful functions (function with  returntype)
def add(a,b):
    return a+b
c = add(10,20)

def sub(a,b):
    return a - b
d = sub(10,20)

print(c*d)

#Recursion(function calling itself)
#syntax: def,function name,condition,recursive call
def  facta(n):
    if n<=1:
        return 1
    return n*facta(n-1)
print(facta(5))

#Recursion sum of n numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
print(sum_n(10))

#scope  
c = 20
def add():
    a = 10
    b = 20
    print(a+b+c)
add()

#global function
name = "Sharmila"
def student_details():
    global section
    section = "CSM-C"
    college = "Malla Reddy University"
    s_id = 260
    location = "Tirupati"
    print(name)
    print(section)
    print(college)
    print("S_Id:",s_id)
    print(location)
student_details()
print(section)



#