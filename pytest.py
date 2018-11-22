"""
Learn Python script includes all examples
Author: Bhoopesh Singh
"""




"""print in python"""
print("start to learn Python....\n")

"""if case test"""
print("\tchecking if case (result shuld be five greater than two)")

if 5 > 2: 
    print("\t\tResult: five greter than two\n")
else:
    print("\t\tResult: five is not greater than two\n")


print("\tchecking if case (result shuld be five greater than two)")

if 5 > 2: 
    print("\t\tResult: five greter than two\n")
else:
    print("\t\tResult: five is not greater than two\n")

"""creating variable 
Python has no command for declaring a variable.
(1) A variable is created the moment you first assign a value to it.
(2) Variables do not need to be declared with any particular type and can even change type after they have been set.
example for two type are follows
"""
print("\tvariable declaration")
x = 12						# x is int
y = "bhpoopesh"				# y is string

print("\t\t",x , " " , y) 	# can not use + when printing int

x = "bhpoopesh"				# x is string now

print("\t\t x was int befor now it is ", x, "\n")

""" get Type of var in python """
print("\ttype of  variables")
a = 12
b = 2.3
c = 2j
d = "BHOOPESH"

print("\t\ta is ", type(a))
print("\t\tb is ", type(b))
print("\t\tc is ", type(c))
print("\t\td is ", type(d),"\n")


""" Specify a Variable Type """
print("\tspecifing a variable type")
a = int(12)
b = float(12)
c = str(12)
d = complex(12)

print("\t\t a is ", a, "with type", type(a))
print("\t\t b is ", b, "with type", type(b))
print("\t\t c is ", c, "with type", type(c))
print("\t\t d is ", d, "with type", type(d),"\n")

"""
Note : String literals in python are surrounded by either single quotation marks, or double quotation marks.
'BHOOPESH' is the same as "Bhoopesh"
"""


"""Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. 
However, Python does not have a character data type, 
a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string."""

print("\tString Literals: testing string behaviour as array")

a = "Bhoopesh Singh"

print("\t\tIn bhoopesh first word is ",a[0],
	"second word is",a[1],
	"third word",a[3])
print("\t\tin a get the characters from position 9 to position 15 is ",a[9:14])

b = "                Bhoopesh Singh               "

print("\t\t b without strip ",b)
print("\t\t b with strip ",b.strip())
print("\t\t length of a", len(a))
print("\t\t lower case ", a.lower())
print("\t\t upper case ", a.upper())
print("\t\t replace bhoopesh with uttam ",a.replace("Bhoopesh", "Uttam"))
print("\t\t split string ", a.split(" "),"\n")


""" get Input from keyboard """

print("\tEnter Your Name: ")
i = input()
print("\t\t Your name is " + i)

""" Python Operators """
print("\tEnter a number:")
a = input()
a = int(a)
print("\tEnter another number:")
b = input()
b = int(b)

print("\t\tSum of two number",a+b)
print("\t\tDiff of two number",a-b)
print("\t\tMul of two number",a*b)
print("\t\tDiv of two number",a/b)
print("\t\texpo of two number",a**b)
print("\t\tfloor div of two number",a//b,"\n")


""" Python Collections (Arrays) """
"""There are four collection data types in the Python programming language:
(1) List
(2) Tuple
(3) Set
(4) Dictonary 
"""
print("\tpython list")
myList = ["node","python","bash","c"]

print("\t\tPrint list:- ",myList)
print("\t\tPrint second string of list: ", myList)
myList[3] = "c++"
print("\t\tReplace c with c++ ",myList)
print("\t\tfor loop in list: ", myList)
for x in myList:
	print("\t\t",x)

print("\tlength of myList: ",len(myList)) #length of list

myList.append("perl")
print("\t\t append function result: ",myList)

myList.insert(2,"lua")
print("\t\t after insert: ",myList)


myList.remove("perl")
print("\tremove function: ", myList)

myList.pop()
print("\t\tpop function result: ", myList)

myList.clear()
print("\t\tclear function result: ", myList)

"""del myList
print(myList)"""

myList = list(("node","python","bash","c"))
print("\t\t craete list using list(): ",myList)

print("\t\tcount of the list: ",myList.count("python"))


""" Tuple in python
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
 """

print("\tTuple in python")
myTuple = ("node","python","bash","c")
print("\t\tTuple: ", myTuple)
print("\t\tTuple as array: ", myTuple[2])
"""myTuple[2] = "lua"
rint("\t\tTuple as array: ", myTuple[2])""" #it will give error
print("\t\tlength of tuple: " ,len(myTuple))
del myTuple
myTuple = tuple(("node","python","bash","c"))
print("\t\tcount of python: ", myTuple.count("python"))
print("\t\tindex of python: ", myTuple.index("python"))


""" 
sets in Python 
A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

"""
print("\tSets in Python")
mySet = {"node","python","bash","c"}
print("\t\t Sets: ", mySet)
print("sets in for loop")
for x in mySet:
	print("\t\t",x)

print("\t\t in use in sets","bash" in mySet)

mySet.add("lua")
print("\t\t add() resp: ", mySet)
print(len(mySet))

"""mySet.update(["fefbei","dewdbew"])
print(mySet)"""
