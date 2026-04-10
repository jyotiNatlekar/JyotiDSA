''' a way of solving a problem by havoing a func calling itself
not efficient
stack memory used
we use recursion especially in case we know that problem can be divided into 
similar sub problems
'''
#Factorial Solution
# def factorial(num):
#     if num <= 1:
#         return 1                         #1    ---->|
#     return num * factorial(num-1)        #4*3*2*1<--|
# print(factorial(5))

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return (isPalindrome(strng[1:-1]))
# print(isPalindrome('tacocat'))

# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base,exponent-1)
# print(power(2,0))
# print(power(2,1))
# print(power(2,2))
# print(power(2,3))

#captitalizefirst solution using recursion
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','doll','banana']))

#productofarray solution
# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))

#fibonacci solution
# def fib(num):
#     if(num<2):
#         return num
#     return fib(num-1) + fib(num-2)
# print(fib(4))
    