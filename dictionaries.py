print("-----Dictionaries-----")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


print()
print("-----Accessing value by key-----")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict['brand'])
print(thisdict['year'])
print(thisdict.get("model"))


print()
print("-----Chnage value-----")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["brand"] = "BMW"
print(thisdict)

print()
print("-----loop through a dictionary-----")

for x in thisdict:
	print(x)


print()
print("-----values of a dictionary-----")

for x in thisdict.values():
	print(x)

print()

for x, y in thisdict.items():
  print(x, y)


print()
print("-----Add items to a dictionary-----")

thisdict["color"] = "orange"
print(thisdict)


print()
print("-----Remove items to a dictionary-----")

thisdict.pop("year")
print(thisdict)