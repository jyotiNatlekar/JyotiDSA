#run time -- called exception handling -- we cannot solve error , only handle 
# we can handle multiple exception in single exception
#--- one exception ---
# n1 = int(input("enter first value : "))
# n2 = int(input("enter second value : "))  
# try:
#     print(n1/n2)
# except:
#     print("Cannot divide by zero")
# print("To Be Continue")
 
#--- when there are many exception to write --- 
# try:
#     n1 = int(input("enter first value : "))
#     n2 = int(input("enter second value : ")) 
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Enter only integer value")
# print("To Be Continue")

# --- we can handle multiple exception in single exception ---
# try:
#     a = int(input("enter first value : "))
#     b = int(input("enter second value : "))  
#     print(a/b)
# except(ValueError , ZeroDivisionError) as message:
#     print(message)

# --- if any error come that we dont know then last except will run ---
# try:
#     a = int(input("enter first value : "))
#     b = int(input("enter second value : "))  
#     print(a/b)
# except(ValueError , ZeroDivisionError) as message:
#     print(message)
# except:
#     print("This is default part of except block")

# --- if there is no error , else block will run --- we can use else block in exception
# try:
#     a = int(input("enter first value : "))
#     b = int(input("enter second value : "))  
#     print(a/b)
# except(ValueError , ZeroDivisionError) as message:
#     print(message)
# except:
#     print("This is default part of except block")
# else:
#     print("Everything is ok")

#--- finally block will always executed whether try block generate error or not
# try:
#     a = int(input("enter first value : "))
#     b = int(input("enter second value : "))  
#     print(a/b)
# except(ValueError , ZeroDivisionError) as message:
#     print(message)
# except:
#     print("This is default part of except block")
# finally:
#     print("I will always executed")

#nested try except block
# try:
#     a = int(input("enter first value : "))
#     b = int(input("enter second value : "))  
#     try:
#         print(a/b)
#     except ZeroDivisionError as message:
#         print(message)
# except ValueError:
#     print("Enter only integer value")

# try:
#     a = int(input("enter first value : "))
#     b = int(input("enter second value : "))  
#     print(a/b)
# except(ValueError , ZeroDivisionError) as message:
#     print(message)
# else:
#     print("there are no error in try block")
# finally:
#     print("I will always executed")

#--- count the number which is repeated---
# input = [5,7,8,3,7,8,9,2,3]
# old = []
# new = []
# count = 0
# for i in range(len(input)):
#     if input[i] not in old :
#         old.append(input[i])
#     else:
#         new.append(input[i])
#         count += 1
# print(old)
# print(new)
# print(count)

#find second largest element
# list = [7,3,9,2,8]
# list.sort()
# print(list)
# print("Second largest element is :", list[-2])

# while i<=5:
#     print(i)
#     i = i +1

# username = ""
# password = ""
# while username != "admin" or password != "pass@123":
#     username = input("enter username : ")
#     password = input("enter password : ")

# name = "programming"
# vowels = ['a' , 'e' , 'i' , 'o' , 'u']
# cons = 0
# vowel = 0
# for i in name:
#     if i in vowels:
#         vowel += 1
#     else:
#         cons += 1
# print("number of vowels : ",vowel)
# print("number of consonant : ",cons)

# list = [1,2,2,3,4,2]
# list1 = []
# count = 0
# for i in range(len(list)):
#     if list.count(i)== 1:
#         list1.append(i)
# print(list1)

# input = [2,3,4,5]
# product = 1
# for i in range(len(input)):
#     product = product * input[i]
# print(product)