#identity , membership operator
#when we want to do address comparison -- identity operator
# there are two idetity operator -- 1.Is  2. Is not
a = 10
b = 10
print(a is b) #True
print(a is not b) #False

a = 10
b = 20
print(a is b) #False
print(a is not b) #True


#used to check whether object is present or not in collection of data structure like(list,tuple,set,dict,string) -- membership operator
#there are two membership operator -- 1.in   2.not in
name = "help4code"
print("z" in name)
print("p" in name)

name = "help4code"
print("z" not in name)