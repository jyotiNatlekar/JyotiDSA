# dict = {"name":"jyoti" , "age" : 30}
# for x in dict:
#     if x == "age":
#       print("key : ",x)
#       print("key exists")

input = [1,2,2,3,4,3,5]
frequency = {}
count = 0
for i in range(len(input)):
    if i not in frequency:
        frequency[i] = frequency[i] + 1
    elif i in frequency:
        count += 1
print(frequency)
print(count)
#op -- {1: , 2: }