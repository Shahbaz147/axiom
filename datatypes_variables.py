# Numbers

print("-----Numbers-----")

x = 1    # int
y = 2.8  # float
z = 1j   # comple

print(type(x))
print(type(y))
print(type(z))



# Booleans

print("----Booleans----")

print(10 > 9)
print(10 == 9)
print(10 < 9)



# Strings & String Slicing

print("-----Strings + string Methods & String Slicing -----")

print("Hello")
print('Hello')

a = "Hello"

print("Sliced String is :" , a[1:4])
print("Sliced String is :" , a[0:4:3])
print("Sliced String is :" , a[-4:-2])
print(len(a))

a = "  Hello world  "

print(a.strip())
print(a.split(" "))
print(a.upper())
print(a.lower())
print(a.replace('o','oo'))

print()
print("-----Check String----")

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

print()
print("---String Concatenation---")
a = "Hello"
b = "World"
c = a +" "+ b
print(c)



# Operators
print()

print("------operators------")

"""
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""

x = 5
y = 3

print("-----Arithmetic operators-----")
print(x + y)
print(x / y)
print(x // y)
print(x * y)
print(x - y)


print("-----Comparison operators-----")
print(x == y)
print(x != y)
print(x > y)
print(x < y)


print("-----Logical operators-----")
print(x > 3 and x < 10)


print("-----Identity operators-----")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


print("-----Membership operators-----")

x = ["apple", "banana"]

print("banana" in x)
print("banana" not in x)



