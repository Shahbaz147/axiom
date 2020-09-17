print("------Lists in Python------")
print()

thislist = ["apple", "banana", "cherry"]
print(thislist)

print()
print("------Access Lists items------")

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print(thislist[-1])


print()
print("------Range of Indexes------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

print()
print("------Change value in list------")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


print()
print("------loop through list------")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print()
print("------if item in list------")

thislist = ["apple", "banana", "cherry"]
if "cherry" in thislist:
   print("Yes, 'cherry' is in the fruits list")

print()
print("------length of list------")

print(len(thislist))

print()
print("------Add item to list------")

thislist.append("Orange")
print(thislist)

print()
print("------Insert at specific index to list------")

thislist.insert(2,"Apple")
print(thislist)



print()
print("------Remove from list------")

thislist.remove("Apple")
print(thislist)
del thislist[0]
print(thislist)


print()
print("------list Comprehension------")

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]

print(common_num)