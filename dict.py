#dict --  represent as key-value pair mutable reprsent by {}
mydict = {
    101 : "Jyoti",
    102 : "vijay",
    103 : "vrushali",
    "104" : "vaishnavi",
    105 : "vandana",
    101 : "atharv",            #it update value of key
    104 : "atharv",
}
print(mydict)

#---with the help of key we have to print values---
# a = mydict[102]
# print(a)

#---we will replace old value by new value---
# mydict[102] = "Papa"
# print(mydict)

#---only print key---
# for x in mydict:
#     print(x)

#---only print values---
# for x in mydict.values():
#     print(x)

#---print both key and value---
# for x,y in mydict.items():
#     print(x,y)

#---if i have to add new key value pair---
# mydict["mobile_no"] = 1234567894
# print(mydict)

# a = {(1,2):1 , (2,3):2 , (4,5):3}
# print(a[4,5])

# a = {'a':1, 'b':2, 'c':3}
# print(a['a','b'])

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,1,2)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(box)
# print(jars)
# print(crates)
# print(len(crates))
# print(len(crates[box]))

# dict = {'c':97 , 'a':96 , 'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# rec = {"Name":"Python" , "Age":"20"}
# r = rec.copy()
# print(id(r) == id(rec))
# print(id(r))
# print(id(rec))

# rec = {"Name":"Python" , "Age":"20" , "Addr":"NJ" , "country":"USA"}
# id1 = id(rec)
# print(id1)
# del rec
# rec = {"Name":"Python" , "Age":"20" , "Addr":"NJ" , "country":"USA"}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)

# dict = {"X":20 , "Y":10 , "Z":30}
# for k in dict:
#     if dict[k] == min(dict.values()):
#         print("small value :",k)
# print(min(dict.values()))
   
#---to remove specific key-value pair we can use pop()---
# mydict = {
#     101 : "jyoti",
#     "professional" : "student"
# }
# mydict.pop(101)
# print(mydict)

