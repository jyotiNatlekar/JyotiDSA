#WAP to accept any one no and check pos,neg and zero
#if check all the if statement ,even if first statement become true 
number = int(input("enter a number : "))
if number > 0 :
    print("It is a positive number")
if number < 0 :
    print("It is a negative number")
if number == 0 :
    print("number is zero")

#WAP
no1 = 10
no2 = 20
no3 = 30
no4 = 40
no5 = 50

if no1 > no2 and no1 > no3 and no1 > no4 and no1 > no5:
    print("Max = ",no1)

if no2 > no1 and no2 > no3 and no2 > no4 and no2 > no5 :
    print("Max = ",no2)

if no3 > no1 and no3 > no2 and no3 > no4 and no3 > no5 :
    print("max = ",no3)

if no4 > no1 and no4 > no2 and no4 > no3 and no4 > no5 :
    print("max = ",no4)

if no5 > no1 and no5 > no2 and no5 > no3 and no5 > no4 :
    print("max = ",no5)

#----------------------------------------------------------------

#if-else
username = input("Enter username : ")
password = input("Enter password : ")
if username == password :
    print("login successful")
else :
    print("invalid credential")

'''AP to accept phy,chem,maths subject marks and calculate total and percentage 
and if percentage >= 60 and gender = male so he is eligible for placement else 
eligible for data entry job'''
phy = int(input("enter marks of physics : "))
chem = int(input("enter marks of chem : "))
maths = int(input("enter marks of maths : "))
gender = input("enter your gender(M/F) : ")
total = phy + chem + maths
percentage = total/3
print("Total =",total)
print("Percentage =",percentage)
if percentage >= 60 and gender == "M" :
    print("eligible for placement")
else :
    print("eligible for data entry job")

#---------------------------------------------------------------

#nested if-else
#WAP to accept value a,b,c and find max
a = int(input("enter a number : "))
b = int(input("enter a number : "))
c = int(input("enter a number : "))
if a > b :
    if a > c :
        print("a is max no",a)
    else:
        print("c is max no",c)
else:
    if b > c:
        print("b is max",b)
    else:
        print("c is max",c)

#mon-fri working  sat-sun holiay
day = input("enter a day : ")
if day == "saturday" or day == "sunday" :
    print("its a weekend")
else:
    print("its a working day")

#------------------------------------------------------

#if-elif-else
#upper, lower,special case
a = ord(input("enter a character : "))
if 65 <= a <= 91 :
    print("YOUR CHARACTER IS IN UPEERCASE")
elif 97 <= a <= 122:
    print("your character is lowercase")
elif 48 <= a <= 57 :
    print("your entered character is digit")
else:
    print("youe character is a special symbol")

#----------------------------------------------------------

#WAP for change calculation with respect to total amount
Amount = int(input("please enter a amount for withdraw : "))
print("100 notes = ", Amount // 100)
print("50 notes = ", (Amount % 100) // 50 )
print("20 notes = ", ((Amount % 100) % 50) // 20)
print("10 notes = ", (((Amount % 100) %50) % 20) // 10)
print("5 notes = ", ((((Amount % 100) % 50) % 20) % 10) // 5)