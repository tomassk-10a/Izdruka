######## map

def nosauk(x):
    return x**2

print(nosauk(6))
print(nosauk(7))
print(nosauk(8))
print(nosauk(9))

print()

skaitli = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
print(map(nosauk, skaitli)) #neder, jo nepiecišama iterācija


print()

for inguss in map(nosauk, skaitli):
    print(inguss)

print()

print(list(map(nosauk, skaitli)))

print()
print("____________________________________________________________________________")
print()
###########################################################

def paris(vards):
    if len(vards) % 2 == 0:
        return "pāra"
    else:
        return vards[0]

print(paris("roka"))
print(paris("rokas"))

print()

vardi =["roka", "mamma", "Ņikita", "pods", "xdd"]
print(list(map(paris, vardi)))

print()
print("____________________________________________________________________________")
print()

################################################################
def mm(sk):
    return sk % 2== 0

print(mm(8))





