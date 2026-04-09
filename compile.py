# compile() function 
# import re    #re module for performing all the regular expression based
# count = 0    #to count the number of matching found
# pattern = re.compile("function")  #string converts into bytecode
# #print(pattern)
# matcher = pattern.finditer("A function in python is define by def statement A function is best to use as function is simple it is widely used.")
# #print(matcher)
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences : ", count)

# --- without compile() --- 
# import re    #re module for performing all the regular expression based
# count = 0
# matcher = re.finditer("hi",'hihihihi')
# #print(matcher)
# for i in matcher:
#     count += 1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurrences : ", count)

import re
obj = input("Enter any character : ")
objmatch = re.finditer(obj,"a7b @k9z")
for match in objmatch:
    print(match.start(),"...",match.end(),"...",match.group())