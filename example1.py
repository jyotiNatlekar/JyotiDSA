#swapping of two numbers using third variable
# val1 = int(input("enter a number val1 : "))
# val2 = int(input("enter a number val2 : "))
# print("number before swapping are : val1 =", val1, "val2 =",val2)
# temp = val1
# val1 = val2
# val2 = temp
# print("Number after swapping are : val1 =", val1, "val2 = ", val2)

#swapping of two number without using third variable
# a = int(input("enter a number a : "))
# b = int(input("enter a number b : "))
# print("number before swapping are : A =", a, "B =",b)
# a = a+b
# b = a-b
# a = a-b
# print("Number after swapping are : A =", a, "B = ", b)

#calculate percentage
# a1 = int(input("enter the marks of subject1 : "))
# a2 = int(input("enter the marks of subject2 : "))
# a3 = int(input("enter the marks of subject3 : "))
# total = a1+a2+a3
# percentage = total/3
# print("Total = ", total)
# print("Percentage = ",percentage)

#calculate simple interest
# p_amount = int(input("Enter a principal amount : "))
# R = int(input("Enter a rate of interest : "))
# T = int(input("Enter the duration of loan amount : "))

# si = p_amount * R * T / 100
# print(si)

#enter height of user in feet and convert to inch and centi
# h = int(input("enter the height of user in feet : "))
# inch = h*12       #5*12 = 60
# cm = inch*2.54    #60*2.54 = 152.4
# print("height of feet in inch :", inch)
# print("height of value in cm : ",cm)

#reverse a number
# num = 123
# a = num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# rev = a*100 + b*10 + c*1
# print(rev)

#swapp 123456
num = 123456
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
f = num // 10
rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f*1
print(rev)

