"""   A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).   """


""" With the for loop we can execute a set 
of statements, once for each item in a list, tuple, set etc.  """

print("-------Loop for each item-------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print()
print("-------Looping Through a String------")
for x in "Axiom":
  print(x)


print()
print("-------Break statement------")

fruits = ["Ali", "Shahbaz", "Ahmad"]
for x in fruits:
  print(x)
  if x == "Shahbaz":
    break


print()
print("-------The continue Statement------")

fruits = ["Ali", "Shahbaz", "Ahmad"]
for x in fruits:
  if x == "Shahbaz":
    continue
  print(x)

print()
print("-------range() Function------")

for x in range(6):
  print(x, end=" ")
print("\n")

for x in range(2, 6):
  print(x, end=" ")
print("\n")

for x in range(2, 30, 3):
  print(x, end=" ")
print("\n")

print()
print("-------Nested Loops------")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


print()
print("-------While Loop------")

i = 1
while i < 6:
  print(i, end=" ")
  i += 1
print("\n")



