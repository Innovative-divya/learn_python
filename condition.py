#Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

#The "in" operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent.
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#we can also use is operator
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#not operator
print(not False) # Prints out True
print((not False) == (False)) # Prints out False