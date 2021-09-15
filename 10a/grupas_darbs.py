#2. grupa.
#...

mylist = [x for x in range(0, 11)]
print(mylist)
mylist = [x**2 for x in range(0, 11)]
print(mylist)

#...
print()

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist)
mylist = [0*0, 1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7, 8*8, 9*9, 10*10]
print(mylist)

#...
print()
mylist = []
for x in range(0,11):
    mylist.append(x**2)
print(mylist)