''' encapsulation --- is a process of protecting the data and functionality
    _a(protected)   
    __a(private)'''

# class Base:       #parent class
#     def __init__(self):
#         print("Parent class constructor called ")
#         self.a = "Jyoti"            #public data member
#         self.__c = "Vrushali"       #private member

# #creating a derived class/child class
# class Derived(Base):
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         # print("calling private member of base class : ")
#         # print(self.a)
#         # print(self.__c)
# obj1 = Derived()
# print(obj1.a)
# print(obj1.__c)      #private data member not accessible 
#obj2 = Base()
#print(obj2.a)
#print(obj2.__c)

# ---how to protect functionality ---
class Rbi:
    #declaring public method
    def publicPolicy(self):
        print("Check the public policy of RBI")
    
    #declaring private method
    def __privatePolicy(self):
        print("There is some private policy which is not accessible for public")

class Sbi(Rbi):
    def __init__(self):         #first sbi class const called
        Rbi.__init__(self)      #second parent class constr called

    def callingPublicMethod(self):      #child class public method
        print("\nInside child class ")
        self.publicPolicy()             #calling parent class public method

    def callingPrivateMethod(self):        #child class private method
        self.__privatePolicy()               #calling parent class private method

# obj1 = Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicPolicy()
# obj1.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2.__privatePolicy()

# obj2 = Rbi()
# obj2.publicPolicy()
# obj2._Rbi__privatePolicy()