#typecasting
val1  = int(input("enter value of val1 : "))
val2  = int(input("enter value of val2 : "))
print(val1 + val2)

#for converting into integer
print(int(3.14))
#we cannot complex value to int
#print(int(10+5j))
print(int(True)) #1
print(int(False))#0
#we cannot convert floating value string or to int
#print(int("4.22"))
print(int("4"))
#we cannot convert string name to int
#print(int("jyoti"))

#for converting into float
print(float(3))#3.0
#we cannot convert complex value to float
#print(float(50+2j))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))
#we cannot convert string name to float
#print(float("name"))

#complex() used to convert
print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex("5"))
print(complex("5.6"))
print(complex("name"))
print(complex(5,-3))
print(complex(True,False))

#bool() is used to convert
print(bool(0))#false
print(bool(15))#true
print(bool(3.14))#true
print(bool(0.0))#false
print(bool(1+2j))#true
print(bool(0+0j))#false
print(bool(-1))#true
print(bool(False))
print(bool(True))
#print(bool(jyoti))#true
print(bool())