# --- match() = it always match only starting or beginning of string with given pattern
# import re
# a = input("Enter string to perform match operation : ")
# mtch = re.match(a,"python is a important language")
# print(mtch)
# if mtch != None:
#     print("match found at beginning level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there is no matching at beggining level")

# --- fullmatch() --- when we have to match full string with given pattern 
import re
a = input("Enter string to perform match operation : ")
mtch = re.fullmatch(a,"pythonisaimportant")
print(mtch)
if mtch != None:
    print("match found at beginning level")
    print(mtch.start()," ",mtch.end())
else:
    print("there is no matching at beggining level")