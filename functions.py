print("-----Function creation-----")

def name_of_function():
	# task you want to do will be defined in the body of function
  print("Hello from a function")


# After you created a function you will have to call it for performing a task
name_of_function()

print()
print("-----Function Arguments-----")

def my_function(fname):
  print(fname + " World")

my_function("Axiom")


# Parameters and Arguments are same things
print()
print("-----Function Parameters-----")
def add(a,b):
  print(a+b)

add(20,10)


print()
print("-----Function Parameters *args-----")

"""  If you do not know how many arguments that will be 
passed into your function, add a * before the parameter name 
in the function definition. """

def add(*ints):
  sum=0
  for i in ints:
  	sum = sum + i
  print(sum)

add(20,10,30,3)


print()
print("----- Keyword Arguments, **kwargs-----")

"""  If you do not know how many keyword arguments that will 
be passed into your function, add two asterisk: ** before the 
parameter name in the function definition. """

def my_function(**strs):
  # print(kid['fname'] + kid['lname'])
  print(strs['fname'] + strs['lname'] + strs['soft'] )

# my_function(fname = "Axiom", lname = " World")
my_function(fname = "Axiom", lname = " World", soft = " Software Company")


print()
print("----- Lambda Function-----")

sum = lambda a,b : a+b

print(sum(15,8))

a = lambda x: x+10

print(a(15))



print()
print("----- Function as Arguments-----")

def add(a,b):
	return a+b

def sum(func,a,b,c):
	z = func(a,b)
	sum = z+c
	return sum

print(sum(add,5,4,3))


