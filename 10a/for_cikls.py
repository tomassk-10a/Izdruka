x = [1, 2, 3, 4]
for varde in x:
    print(varde)
print()
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for mamma in y:
    print(mamma)
print()

y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for _ in y:
    print("sveiki")
print()

for sk in y:
    if sk % 2 == 0:
        print(sk)
    else:
        print(f"nepara skaitlis: {sk}")
print()

sum = 0
for sk in y:
    sum=sum+sk
print(f"summa pec {sk} skaitliem ir {sum}")
print(sum)
print()
f = "Sveika pasaule"
for tet in f:
    print(tet)

print()

for tet in "programma":
    print(tet,end=" ")

print()

tup = (1, 2, 3, 4)
for elements in tup:
    print(elements)

print()
mylist = [(1,2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(len(mylist))
for elements in mylist:
    print(elements)
print()
for (a, b) in mylist:
    print(a)
    print(b)
print()

   