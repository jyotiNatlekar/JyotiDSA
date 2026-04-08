'''abstraction --- a class which contain atleast one or more abstarct method
abstarct method is a method that has a declaration not have implementation,
child class have implementation
python does not directly supoort abstraction we have to import abc(abstractBaseClass)
'''
# from abc import ABC,abstractmethod      #abstractbasemethod
# class Help4code(ABC):    #abstract class
#     @abstractmethod      #decorator
#     def training(self):    #abstract method
#         pass

#     def placement(self):
#         pass

# class Jyoti(Help4code):
#     def training(self):
#         print("C , C++ , Java")
#     def placement(self):
#         print("Java placement")

# class Vrushali(Help4code):
#     def training(self):
#         print("Python  |  Django")
#     def placement(self):
#         print("Python placement students")

# class vaishnavi(Help4code):
#     def training(self):
#         print("Machine learning")
#     def placement(self):
#         print("data science placement")

# obj1 = Jyoti()
# obj1.training()
# obj1.placement()

# obj2 = Vrushali()
# obj2.training()
# obj2.placement()

# obj3 = vaishnavi()
# obj3.training()
# obj3.placement()

# from abc import ABC,abstractmethod
# class Irctc(ABC):
#     @abstractmethod
#     def bookTicket(self):
#         pass

# class MakeMyTrip(Irctc):
#     def bookTicket(self):
#         print(" ============================================= ")
#         print(" Welcome to makemytrip.com   ")
#         source      = input("Enter a source station name : ")
#         destination = input("Enter destination name : ")
#         date        = input("Enter date : ") 
#         print(" ============================================= ")

# class GoIbibo(Irctc):
#     def bookTicket(self):
#         print(" Welcome to GOIBIBO   ")
#         source      = input("Enter a source station name : ")
#         destination = input("Enter destination name : ")
#         date        = input("Enter date : ") 
    
# class RedBus(Irctc):
#     def bookTicket(self):
#         print(" Welcome to Resbus   ")
#         source      = input("Enter a source station name : ")
#         destination = input("Enter destination name : ")
#         date        = input("Enter date :") 
        
# obj1 = MakeMyTrip()
# obj1.bookTicket()

# obj2 = GoIbibo()
# obj2.bookTicket()

# obj3 = RedBus()
# obj3.bookTicket()
        
