
def eat():
    print("hello")
    print("lol")
eat()
eat()
print()

def funkcijas_nosaukums(arguments1, arguments2):
  print("Sveiki", arguments1, arguments2) #funkcijas darbības

funkcijas_nosaukums("Marcelo",12)
funkcijas_nosaukums("Martin",12)
#funkcijas_nosaukums()
#funkcijas_nosaukums()
print()

def auto(arguments1,arguments2):
    print(f"Šī {arguments2} automašīna ir {arguments1}")
auto("Audi","ātrā")
auto("Nissan","zaļa")
print()

def saskaiti_skaitlus(sk1,sk2):
  return sk1 + sk2

rezultats1 = saskaiti_skaitlus(2,7)
#print(rezultats1)
rezultats2 =saskaiti_skaitlus(1,3)
#print(rezultats2)
rezultats3 = saskaiti_skaitlus(1, 3.5)
print(rezultats1 * rezultats2 + rezultats3)
print()

#
def parbaudi_pari(skaitlis):
    rezult = skaitlis%2==0
    return rezult
    
print(parbaudi_pari(41))
print(parbaudi_pari(44))
print()
#
def parbaudi_pari_list(saraksts):
    for skaitlus in saraksts:
        if skaitlus % 2 == 0:
            return True
        else:
            pass
    return False

print(parbaudi_pari_list([1, 2, 3, 7]))
print(parbaudi_pari_list([1, 5, 3, 7]))

print("______")
print()
def parbaudi_pari_list2(saraksts):
    para_skaitli = []
    for skaitlus in saraksts:
        if skaitlus % 2 == 0:
            para_skaitli.append(skaitlus)
        else:
            pass
    return para_skaitli

print(parbaudi_pari_list2([1, 2, 3, 4, 5]))
print()

