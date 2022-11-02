# list
selectname = "Dan"
listname = ["gg","Dan","aa"]
if selectname in listname:
    print("yes its in")

listname.append("test")
print(listname)
listname[2]=55
print(listname)
print(len(listname))
listname.insert(2,"new text")
print(listname)
listname.insert(2,"new text")
print(listname)
listname.remove("new text")
print(listname)
listname.remove("new text")
print(listname)
listname.pop(1)
print(listname)


# tuple is a sequence of python objects that you cannot change
myTuple = ("python", 50,"var")
print(myTuple)