#1. uzd
mystring = "abcdefghijklmnoprstuvz"
x = mystring[2:6]
print(x)

print()

#2.uzd
y = input("Ievadi jebkādu vārdu!: ")
print(y.upper())

print()

#3.uzd
a = str(input("Ievadi pirmo skaitli: "))
b = str(input("Ievadi otro skaitli: "))
if a>b:
    print(f"Skaitlis {a} ir lielāks par skaitli {b} .")
elif b>a:
    print(f"Skaitlis {b} ir lielāks par skaitli {a} .")
else:
    print(f"Skaitlis {a} ir vienāds ar skaitli {b} .")

print()


#4 uzd.
mylist = [5, 7, 6, 8, 25, -4, 3]
mylist_summa = sum(mylist)
print(mylist_summa)

print()


#5.uzd
gg = input("Ievadi savas klases skaitli: ")
print(f"Es mācos {gg}. klasē.")

print()

#7.uzd
#Izveido funkciju, kas pārbaudīs vai skaitlis dalās ar 2, vai nedalās. Ja dalās izdod true, ja nedalās tad False.

def para_sk(skaitlis):
    dalas = skaitlis%2==0
    return dalas
    
print(para_sk(186))
print(para_sk(11))










