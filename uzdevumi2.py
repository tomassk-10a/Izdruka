# 1.uzdevums
a=15
b=2.5
c=4.78
if a > b and a > c and b < a and b < c:
    print("Skaitlis a ir vislielākais un skaitlis b ir vismazākais.")
elif a < b and a < c and b > a and b > c:
    print("Skaitlis b ir vislielākais un skaitlis a ir vismazākais.")
else:
    print("Pārbaudi mainīgo saturu!")
print()

# 2.uzdevums
temp = float(input("Ievadiet savu temperatūru: "))
print()
if temp < 35:
    print("Vai nav par aukstu?")
elif 35 <= temp <= 37:
    print("Viss kārtībā")
else:
    print("Iespējams drudzis!")

