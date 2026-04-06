'''1.overloading --- python does not support method , constructor overloading
it only support operator overloading'''
#method overloading
# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj = Arithmetic()
# obj.add(10)
# obj.add(5,20)
# obj.add(1,2,4)

#it can handle by default argument
# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None:
#            print(a+b)
#         elif a!=None and b!=None and c!= None:
#             print(a+b+c)
#         else:
#             print("enter atleast two argument")
# obj = Arithmetic()
# obj.add(10)
# obj.add(10,20)
# obj.add(1,2,4)

# --- constructor overloading -- 
# class Arithmetic:
#     def __init__(self):
#         print("there is no argument")
#     def __init__(self,a):
#         print("passing one argument")
#     def __init__(self,a,b):
#         print("passing two argument")
# obj = Arithmetic()
# obj = Arithmetic(10)
# obj = Arithmetic(2,2)

''' --- python supoort overriding  1. method  2.constructor
there must parent and child relationship  
using super() method u can access the parent class method into child class method'''
# class Rbi:
#     def Home_loan(self):
#         print("Home loan = 7.5")

#     def carLoan(self):
#         print("Car loan 8%")

# class Sbi(Rbi):
#     def Home_loan(self):
#         print("Sbi provide home loan = 6.5")
    
#     def carLoan(self):
#         print("car loan is 6%")       
#         return super().carLoan()      #it will return original value also

# obj = Sbi()
# obj.Home_loan()   #child class method override parent class method
# obj.carLoan()

# --- constructor overriding ---
class Father:
    def __init__(self):
        print("Father := i am already at breakfast table")
    
class Child(Father):
    def __init__(self):
        print("Child := i will be late for breakfast")
        super().__init__()
obj = Child()