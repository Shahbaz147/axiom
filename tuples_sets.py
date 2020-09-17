print("A tuple is a collection which is ordered and unchangeable.")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple[2:5])
print(thistuple[-1])
print(thistuple[1])

print()
print("we can change tuple value by changing it to list then again we can change it to tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print()

print("-----loop through tuple------")
x = ("apple", "banana", "cherry")

for x in x:
	print(x)


print()
print("A set is a collection which is unordered and unindexed")
print()



thisset = {"apple", "banana", "cherry"}
print(thisset)

print()
print("----Loop through set----")
for x in thisset:
  print(x)

print("banana" in thisset)

print()
print("----add item to set----")

thisset.add("orange")    # to add one item to set
print(thisset)
thisset.update(["orange", "mango", "grapes"])     # to add multiple items to set
print(thisset)


print()
print("----Remove item from set----")
thisset.remove("banana")
print(thisset)

thisset.discard("orange")
print(thisset)


print()
print("----Union of set----")

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,"a"}

set3 = set1.union(set2)
print(set3)


print()
print("----Update of set----")

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3,"a"}

set1.update(set2)
print(set1)