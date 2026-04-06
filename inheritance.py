# pillar of oop --- inheritance,abstraction,polymorphism,encapsulation ---

''' --- inheritance ---  means reusability - var,function
extending property from one class to another class calles inheritance
base class  a class which inherit its property to another called base or parent
derived class a class in which properties are inherited called derived or child
'''

''' ---- 1.single inheritance -- syntax : class derived-class(base-class): -----
 --- child object is created ---   '''
# class College:          #parent class
#     def college_name(self):    #member function of college
#         print("Modern College")

# class Student(College):      #child class
#     def student_info(self):    #member function
#         print("Name :   Jyoti Natlekar")
#         print("Branch : CSE")

# obj = Student()   #object create child class
# obj.college_name()
# obj.student_info()

'''2. multilevel inheritance - syntax : class GrandFather:
class father(GrandFather):
class Child(Father)      
child object is created  '''
# class College:          #first class
#     def college_name(self):    
#         print("Modern College")

# class Student(College):      #second class
#     def student_info(self):  
#         print("Name :   Jyoti Natlekar")
#         print("Branch : CSE")

# class Exam(Student):           #child class
#         def subject(self):
#             print("subject1 : maths")
#             print("subject2 : computer network")
#             print("subject3 : IP")

# obj = Exam()   #object create child class
# obj.college_name()
# obj.student_info()
# obj.subject()

'''3. multiple inheritance -- syntax : class parent1:
class parent2:
class parentN:
class derived(parent1,parent2,....)  '''
# class SubjMarks:    #class1
#     math = int(input("Enter the marks of subject maths : "))
#     IP = int(input("Enter the marks of subject IP : "))
#     C = int(input("Enter the marks of subject C : "))
#     CN = int(input("Enter the marks of subject CN : "))

# class PractMarks:
#     cpract = int(input("Enter practical marks of c language : "))

# class Result(SubjMarks,PractMarks):     #child class
#     #print("if student pass in both = subj and practical paper then pass")
#     def total(self):
#         if self.math >= 40 and self.IP >= 40 and self.C >= 40 and self.CN >= 40 and self.cpract >= 20:
#             print("pass")
#         else:
#             print("fail")
# obj = Result()
# obj.total()

