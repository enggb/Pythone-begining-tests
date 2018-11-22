myDict = {
	"Name": "Bhoopesh",
	"Age": 20,
	"Nature": "Good"
}

print(myDict["Name"])
print(myDict.get("Age"))
myDict["Nature"] = "Gooooood"
print(myDict)
print("#############################################################")
for x in myDict:
	print(x)

print("#############################################################")
for x in myDict:
	print(myDict[x])

print("#############################################################")
for x in myDict.values():
	print(x)

print("#############################################################")
for x, y in myDict.items():
	print(x, y)

print(len(myDict))
myDict["color"] = "fair"
 
print(myDict)

myDict.popitem()
print(myDict)

myDict.clear()
print(myDict)

myDict =dict(Name="Bhoopesh",Age= 20, Nature= "Good")
print(myDict)