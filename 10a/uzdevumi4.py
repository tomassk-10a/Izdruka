#uzd1

#Lietotājs ievada divus veselos skaitļus – intervāla galapunktus. Izdrukāt visus norādītā intervāla skaitļus, ieskaitot abus galapunktus.

#Papilduzdevums - ja norādīts nekorekts intervāls, tad izdrukā attiecīgu paziņojumu

a = int(input("ievadi pirmo ciparu: "))
b = int(input("ievadi otro ciparu: "))
for i in range(a, b + 1):
    print(i)
print()

#uzd2

#Lietotājs ievada veselu skaitli. Aprēķini šī skaitļa faktoriālu, izmantojot ciklu. faktoriāls = 1*2*3*....*n

c = int(input("ievadi ciparu: "))
faktorials = 1
for gg in range(1, c + 1):
    faktorials = faktorials * gg
print(f"Skaitļa {c} faktorials ir {faktorials}")
print()
#uzd3

#No lietotāja ievadīta intervāla, izvadi visus veselos skaitļus, kas dalās ar konkrētu skaitli (arī to norāda lietotājs).

a = int(input("ievadi pirmo skaitli: "))
b = int(input("ievadi otro skaitli: "))
c = int(input("ievadi ciparu ar kuru dalīs: "))

for i in range(a, b + 1):
    if i % c == 0:
        print(i)

#uzd4

#Izvadi ar cikla palīdzību:

# 1

# 12

# 123

# 1234

#uzd5

# Fibonači virknē, katrs nākamais skaitlis ir divu iepriekšējo skaitļu summa: 0 1 1 2 3 5... Izvadi visus Fibonači virknes skaitļus no 1 līdz 100
