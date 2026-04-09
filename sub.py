'''sub() 
this function perform substitution or replacement 
re.sub(expression,replacement,string) here every match pattern will be replaced 
by provided replacement '''
# import re
# obj = re.sub('[A-Za-z]','X','Jyoti 0509')
# print(obj)

'''subn()
similar to sub(),one thing is different that it also return number of replacement.
this return in tuple where first element is string and 
second one is number of replacement'''
# import re
# obj = re.subn('[A-Za-z]','X','Jyoti 05092005 @new')
# print(obj)
# print("the string is : ",obj[0])
# print("the number of replacement is : ",obj[1])

#--- WAP to check the valid mobile number ---
# import re
# mo = input("Enter mobile number : ")
# obj = re.fullmatch("[0-9]\d{9}",mo)
# if obj != None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")

# --- WAP to check email is valid or not --- 
# import re
# s = input("Enter email_id : ")
# m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
# m1 = re.fullmatch("\w[a-zA-Z0-9_.]*@ybit[.]com",s)
# if m != None or m1 != None:
#     print("valid email id")
# else:
#     print("invalid email id")

#--- WAP to check whether file exist or not if exist, print content ---
# import os,sys
# fname = input("Enter file name : ")
# if os.path.isfile(fname):
#     print("file exists :",fname)
#     f = open(fname,"r")
# else:
#     print("file does not exist : ",fname)
#     sys.exit(0)
# print("the content of file is : ")
# data = f.read()
# print(data)