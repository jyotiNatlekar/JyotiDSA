# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)

#--- to remove 0 from list and add it to last---
# A = [4,0,2,5,0,1]
# for i in A:
#     if i == 0:
#         A.remove(i)
#         A.append(i)
# print(A)

#---remove duplicate---
# input = [1,2,2,3,4,4,5]
# output = []
# for i in input:
#     if i not in output:
#         output.append(i)
# print(input)
# print(output)

# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)

# n = int(input("enter size of array : "))
# arr = []
# for i in range(n):
#     val = int(input("enter value of array : "))
#     arr.append(val)
# sum = 0
# print(arr)
# for i in range(n):
#     if i+1 in range(n):
#         sum += abs(arr[i]-arr[i+1])
# print(sum)

# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

#zip() --- inside this we can take multiple range function
# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i," ",j)

# input = "prashant*is*a*good*programmer"
# newname = ''
# val = ''
# for i in input:
#     if i!= '*':
#         newname += i
#     else:
#         val +=i
# print(newname)
# print(str(val+newname))

#BODMAS
# a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)
# print(id(x))
# print(id(y))
# print(id(z))

#anagram
# s1 = "listen"
# s2 = "silent"
# if len(s1) == len(s2):
#     if sorted(s1) == sorted(s2):
#         print("it is anagram")
#     else:
#         print("it is not ")
# else:
#     print("not ")

input = "this is a sentence"
count = 1
for i in input:
    if i == " ":
        count = count+1
print(f"count is : ",count)

