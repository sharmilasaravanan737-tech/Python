#Arithmetic operator
a = 10
b = 20
print("Addition:",a + b)
print("Subtraction:", a - b)
print("Multipilcation:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Reminder:", a % b)
print("Power:", a ** b)


 #simple calculator
a = int(input("enter first number: "))
b = int(input("enter second number:"))

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:",a*b)
print("Division:", a/b)
 
#Sudent Mark Calculator
name = input("enter student name: ")
m1 = int(input("enter python marks:"))
m2 = int(input("enter java marks: "))
m3 = int(input("enter sql marks : "))
total = m1+m2+m3
average = total/3
print("\n----- Student report ----")
print("name:",name)
print("total:", total)
print("average:", average)


#shopping bill calculator
price1 = float(input("enter product 1 price: "))
price2 = float(input("enter procuct 2 price: "))
price3 = float(input("enter product 3 price: "))
price4 = float(input("enter product 4 price: "))
total = price1+price2+price3+price4
discount = total* 0.10
Final_amount = total - discount
print("Discount:",discount)
print("Final_amount:",Final_amount)


#salary calculator
basic = float(input("enter basic salary"))
hra = basic * 20
da = basic * 0.10