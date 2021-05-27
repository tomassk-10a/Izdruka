"""
def procenti(a,b):
    return a*0.1, b*0.2

print(procenti(100, 100))

def var_pagulet(diena):
    if diena>5: 
        return True
    else:
        return False

print(var_pagulet(4))

def merkaki(a, b):
    if a and b:
        return True
    elif a
        return False

print(merkakis())

pirmais = int(input("pirmais:  "))
otrais = int(input("otrais:  "))
print(pirmais+otrais)

def starpiba(n):
    if n<21:
        st = 21-n
    else:
        st = n-21
    if st>21:
        return st*2
    else:
        return st

print(starpiba(4983369))
print()


def papagaila_problema(hour, runa):
    if hour < 7 or hour > 20 and runa:
        return True
    else:
        return False

print(papagaila_problema(13, True))

"""
def poz_neg(a, b, negative):
    if a < 0 and b < 0 and negative:
        return True
    if (a < 0 and b>0 and not negative) or (a>0 and b<0 and not negative):
        return True
    return False

poz_neg(5, -8, False)