"""
#1. uzdevums
n = int(input("ievadi ciparu: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
print()

#2. uzdevums
a = int(input("ievadi pirmo ciparu: "))
b = int(input("ievadi otro ciparu: ")) 
if a<b:
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
 
print()

#3. uzdevums
n = int(input("ievadi veselu ciparu: "))
for i in range(n, 0-1, -1):
  if i % 2 == 0:
      print(i)
"""
#4. uzd.
my_list = []
for i in range(3):
    n = float(input(f"Ievadi {i+1}. skaitli: "))
    my_list.append(n)
    print(my_list)


#5. uzd.
