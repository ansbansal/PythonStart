# print ("hello world")
Name = input("what is your name")
Neighbours = input("what is your neighbour's name")
Codingtime = int(input("how long have you been coding"))
NeighbourCodingTime = int(input("how long have your neighbour been coding"))

totaltime = Codingtime+NeighbourCodingTime

print("my name is " + Name)
print("my neighbour's name is " + Neighbours)
print("me and neighbour have been coding together for", totaltime)


# if loops
x=5
y=15
if x==1:
    print("x is equal to 1")
elif x>5:
    if y>10:
        print("x is greater than 5 and y is greater than 10")
    else:
        print("x is greater than 5 and y is less than or equal to 10")
elif y>10:
    print("x is less than or equal to 5 and y is greater than 10")
else:
    print("x is less than or equal to 5 and y is less than or equal to 10")




