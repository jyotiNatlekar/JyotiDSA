'''tuple -- orderwise , negative index, heterogeneous, reprsent by (), 
duplicate value allow, list by nature is growable, immutable '''
# mytuple = ("jyoti" , "vijay" , "Anamika" , "vrushali" , "vaishnavi" , "vrunda" , "arya" , 23 , 23.5 , "Vandana")
# print(mytuple)
# print(type(mytuple))

# mytuple[2]="vandana"         #it cannot execute bcz tuple is immutable
# print(mytuple)

# init_tuple = ()                  
# print(init_tuple.__len__())

# init_tuple_a = 'a' , 'b'
# init_tuple_b = ('a' , 'b')
# print(init_tuple_a == init_tuple_b)
# print(id(init_tuple_a))
# print(id(init_tuple_b))

# init_tuple_a = '1' , '2'
# init_tuple_b = ('3' , '4')
# print(init_tuple_a + init_tuple_b)

# init_tuple = ('Python') * 3     #it is string
# print(type(init_tuple))

# init_tuple = ('Python',) * 3    # if it has comma then it is tuple
# print(type(init_tuple))

# init_tuple = (1,) * 3   # error bcz tuple is immutable
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1,2),) * 7
# print(len(init_tuple[3:8]))

