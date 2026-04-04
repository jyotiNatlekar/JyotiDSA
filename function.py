#1.buildin  2. user define -- when u want customized 
# def msg():       #define/called function
#     print("Hello World")
# msg()            #calling
# msg()

# def arithmetic():
#     a = int(input("Enter the value of A :"))
#     b = int(input("Enter the value of B :"))
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div
# # print(arithmetic())
# result=arithmetic()
# print("Arithmetic = ",result)

'''how many types of argument we can pass in function?--- 4types 
positional,keyword,default,variable number of argument/variable length argument'''
#positional
# def login(username,password):
#     if username == password:
#         print("LOGIN SUCCESSFUL")
#     else:
#         print("INVALID CREDENTIAL")

# username = input("Enter username : ")
# password = input("Enter password : ")
# login(username,password)               #calling

#keyword
# def login(username,password):
#     if username == password:
#         print("LOGIN SUCCESSFUL")
#     else:
#         print("INVALID CREDENTIAL")
# login(username="admin",password="admin")   

#default
# def cityName(city="Goa"):    #here we set default value
#     print(city)
# cityName("Delhi")
# cityName("Amboli")
# cityName()

#variable length argument/variable number of argument
# def nameOfCitys(*city):      # (* means select all)
#     print("City Names = ",city)
# nameOfCitys("Goa","Amboli","Choukul","Manali","Pune")

#WAP for menu driven code
import sys
def add():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("Add = ", val1 + val2)

def sub():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("Sub = ", val1 - val2)

def mul():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("Mul = ", val1 * val2)

def div():
    val1 = int(input("Enter the value of val1 : "))
    val2 = int(input("Enter the value of val2 : "))
    print("Div = ", val1 / val2)

while True:                       #while is used when how many time used is not known
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        sys.exit()