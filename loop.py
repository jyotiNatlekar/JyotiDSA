#looping
#if range is given -- for loop used
# for i in range(5):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(1,11):
#     print(i*2)

#WAP table of 2 ...... 10
# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5)
# print("------------------------------------------------------------------------")
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14)

# name = "racear"
# for i in name:
#     print(i)

#WAP to remove duplicate
# name = "racear"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname += i
# print("Original String is : ",name)
# print("After removing duplicate character : ",newname)

# for i in range(5,0,-1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

#WAP to reverse a string using for loop
# name = "Mumbai"
# newname = ""
# n = len(name)
# for i in range(n-1,-1,-1):
#     newname += name[i]
# print(newname)

#WAP to check if given string is palindrome
input = "racecar"
output = ""
for i in range(len(input)-1,-1,-1):
    output += input[i]
if input == output:
    print(input)
    print(output)
    print("it is palindrome")
else:
    print("it is not a palindrome")
#-------OR -------
name  = "racecar"
print(name)
print(name[::-1])
if name == name[::-1]:
    print("palindrome string")
else:
    print("not palindrome string")
