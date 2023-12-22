#data type in python
#1.number
    #int
myint = 7
print(myint)
    #float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
#2.string
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
    #OR
mystring = "Don't worry about apostrophes"
print(mystring)

#exercise: create a string, an integer, and a floating point number.
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

