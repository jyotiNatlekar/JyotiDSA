
# --- class --- first letter of classname is capital
# class Student:
#     rollno = 101                         #data member
#     def studentData(self):               #method/member function
#         print("Student information")

# obj = Student()                     #obj is also called reference variable
# print(obj.rollno)
# obj.studentData()

# class Demo:
#     def __init__(self):
#         print("I am constructor")

#     def msg(self):
#         print("Hello clas!")
# obj1 = Demo()
# print(obj1)
# obj2 = Demo()

# class Hod:
#     def __init__(self):
#         self.name = 'Jyoti natlekar'
#         self.age = 20
#         self.studid = 39
#     def info(self):   #instance method
#         print("My name is : ",self.name)
#         print("My age is : ",self.age)
#         print("My student id : ",self.studid)
# obj = Hod()   #object create
# obj.info()

# class Hod:
#     def __init__(self,name,age,rollno):   #parameterize constructor
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#     def info(self):   
#         print("name : ",self.name)
#         print("age : ",self.age)
#         print("rollno : ",self.rollno)
# obj = Hod('Jyoti' , 20 , 39)   
# obj.info()

#--- types of variable --- instance,static 
#instance 
# class New:
#     def __init__(self):
#         self.a = 10
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

# Obj1.a = 20
# print()

# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

#where we can declare instance var
#declaring instance variable outside the class by using object
# class Student:
#     def __init__(self):       #constructor
#         self.s_name = 'jyoti'
#         self.s_rollno = 39        #declaring a instance var inside a constructor
#     def getdata(self):
#         self.s_mb = 23247394639   #declaring a instance var inside a instance method
# obj = Student()
# obj.getdata()
# del obj.s_mb               #delete the instance variable using obj
# obj.s_branch = 'CSE'       #adding instance variable by using obj
# print(obj.__dict__)

# --- static variable --- 
# 1 static var = 1 memory
# class New:
#     a = 10
#     def __init__(self):
#         self.name = "jyoti"     #instance var
# obj1 = New()
# obj2 = New()
# obj3 = New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a = 60
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# --- instance method ---
# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name = name       #instance variable
#         self.rollno = rollno
#         self.mob = mob
#     def display(self):       #instance method
#         print(self.name," ",self.rollno," ",self.mob)
# stud = Student("jyoti",39,893402493)
# stud.display()
        
# --- static method ---
# class Student:
#     # -- by using class name we can access static method
#     @staticmethod   #decorator
#     def get_personal_detail(firstname,lastname):
#         print("your personal details = ",firstname,lastname)

#     @staticmethod
#     def contact_detail(mobil_no, rollno):
#         print("your contact detail = ",mobil_no,rollno)

# Student.get_personal_detail("Jyoti","natlekar")
# Student.contact_detail(782659870,39)


