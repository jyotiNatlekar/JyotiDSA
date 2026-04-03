#collection datatype
'''list --- orderwise , negative index, heterogeneous, reprsent by [], 
duplicate value allow, list by nature is growable, mutable'''
# mylist = ["jyoti","Vijay","Natlekar",5,9,2005,05.18,"good"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist[2]="Vrushali"
# print(mylist)

# if "Vrushali" in mylist:
#     print("YES vrushali is available")
# else:
#     print("NO vrushali is not available")

#append add element at end of list
# mylist.append("Natlekar")
# mylist.append("Vaishnavi")
# mylist.append(5)
# print(mylist)

# mylist.insert(2,"vaishnavi")
# print(mylist)

# mylist.remove("Vijay")
# print(mylist)

# newlist = mylist.copy()
# print(mylist)
# print(newlist)

#nested list --- called multidimensional array
'''       0         1
0 =   ["jyoti" ,  "Natlekar"]
1 =   [  5 ,          18]
2 =   ["good" ,     2005]
'''
# mylist = [["jyoti","Natlekar"] , [5 , 18] , ["good" , 2005]]
# print("example of multidimensional list : ")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[1][1])
# print(mylist[2][0])
# print(mylist[2][1])

#---to show list multiple time---
# list1 = ['jyoti' , 'natlekar']
# print(list*2)

#---to add 2list---
# list2 = [5 , 9 , 2005]
# print(list1 + list2)

#---delete list---
# list2 = ['jyoti','natlekar']
# del list2
# print(list2)
#----to delete specific index value----
# del list2[0]
# print(list2)

#---to represent empty list---
# list2 = ['jyoti' , 5]
# list2.clear()
# print(list2)

#---list constructor---
# name = "jyoti"
# print(name)
# myname = list(name)  #typecasting
# print(myname)

#---to reverse a list---
# mylist = [ 5 , 18 , "jyoti"] 
# mylist.reverse()
# print(mylist)

#---sorting--- when sorting list should be homogeneous(one dataype value)
'''default sorting order for number is ascending order
default sorting order for string is alphabet order
'''
# mylist = [10,20,18,77,90,3,1,5]
# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)     #---if reverse=True then it sort in decending order---
# print(mylist)

#list alising
#assigning one variable reference to another 
# mylist = ["jyoti" , 5 , 18]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist[1] = "Natlekar"
# print(mylist)
# print(newlist)

#---pop() remove last element---
# arr =[[1,2,3,4],
#       [4,5,6,7],
#       [8,9,10,11],
#       [12,13,14,15]]
# for i in range(0,4):   #---outer for loop is used for row---
#     print(arr[i].pop())

# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ")

# fruit_list1 = ['Apple', 'Berry']


#
# a = [1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a = [1,2,3,4,5]
# print(a[3:0:-1])

