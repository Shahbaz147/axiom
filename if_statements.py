"""
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b)
"""


print("-----if Statement------")
a = 33
b = 200
if b > a:
  print("b is greater than a")

print()

print("-----if-Else Statement------")

a = 33
b = 200
if b > a:
  print("b is greater than a")
else:
  print("a is greater than or equal to b")

print()

print("-----if-elif-Else Statement------")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif b == a:
  print("b is equal to a")
else:
  print("b is less than a")

print()
print("-----Short Hand If ... Else----")
a = 5
b = 3
c = a if b > a else b
print(c)


print()
print("-----And----")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


print()
print("-----or----")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print()
print("-----Nested if----")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



