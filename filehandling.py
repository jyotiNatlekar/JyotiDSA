#--- two types of file -- text file , binary file ---
# f = open("myfile.txt" , "w")
# print("name of file : ",f.name)
# print("file mode    : ",f.mode)
# print("readable     : ",f.readable())
# print("writable     : ",f.writable())
# print("file closed  : ",f.closed)
# f.close()
# print("file closed  : ",f.closed)

#--performing write operation--
# f = open("myfile.txt","w")
# f.write("\npune is a smart city")
# f.close()
# print("file operation is done")

#-- performing append operation -- it also write but it do not override the data it append to it
# f = open("myfile.txt","a")
# f.write("\nsawantwadi is a smart city")
# f.close()
# print("file operation is done")

#inserting list
# f = open("myfile.txt","w")
# mylist = ['jyoti' , 'vijay' , 'natlekar']
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")

#inserting tuple
# f = open("myfile.txt","w")
# mytuple = ('jyoti' , 'vijay' , 'natlekar')
# f.writelines(mytuple)
# f.close()
# print("written work has done successfully")

#inserting dict
# f = open("myfile.txt","a")
# mylist = {'name':'jyoti' , 'age':'vijay'}
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")

#reading data from a file
# f = open("myfile.txt","r")
# print(f.read())
# f.close()

# with open("myfile.txt","w") as f:
#     f.write("vaishnavi\n")
#     f.write("jyoti\n")
#     f.write("vrushali\n")
#     print("file closed : ",f.closed)
# print("file closed : ",f.closed)

# with open("myfile.txt","r") as f:
#     content = f.read()
#     print(content)

# --- binary files --- rb,wb
# f1 = open("screenshot.jpg","rb")
# f2 = open("screen.jpg","wb")
# data = f1.read()
# f2.write(data)
# print("New image is available with the name: ")

#operation with csv file
# import csv
# f = open("student.csv","a",newline="")
# a = csv.writer(f)
# # a.writerow(["studentID","rollno","name","mobileno"])
# studentid = int(input("Enter student id : "))
# rollno = int(input("Enter your roll no : "))
# name = (input("Enter your name : "))
# mobileno = int(input("Enter your mobile no : "))
# a.writerow([studentid,rollno,name,mobileno])
# print("student record has save")

import csv
f = open("stud1.csv","a",newline="")
a = csv.writer(f)
# a.writerow(["studentID","rollno","name","mobileno","p1","p2","p3","total","percentage","result"])
studentid = int(input("Enter student id : "))
rollno = int(input("Enter your roll no : "))
name = (input("Enter your name : "))
mobileno = int(input("Enter your mobile no : "))
p1 = int(input("enter a marks of sub1 : "))
p2 = int(input("enter a marks of sub2 : "))
p3 = int(input("enter a marks of sub3 : "))
total = p1+p2+p3
percentage = total/3.0
if p1 >= 40 and p2 >= 40 and p3 >= 40:
    result = "pass"
else:
    result = "fail"
a.writerow([studentid,rollno,name,mobileno,p1,p2,p3,total,percentage,result])
print("student record has save")

