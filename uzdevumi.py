# 1.uzdevums
x = input("Ievadi teikumu!: ")
print(len(x))
print(" ")

# 2.uzdevums
y = input("Ievadi jebkādu vārdu!: ")
print(y[0])
print(" ")

# 3.uzdevums
z = "Sveika, pasaule!"
print(z[10:15])
print(" ")

# 4.uzdevums
q = input("Ievadi teikumu!: ")
print(q.upper())
print(" ")

# 5.uzdevums
w = input("Ievadi teikumu!: ")
print(w.lower())
print(" ")

# 6.uzdevums
e = "samērcēt"
pedBurti = e[1:]
print("p" + pedBurti)
print(" ")

# 7.uzdevums
r = "     Sveika, pasaule!"
print(r.strip())
print(" ")

# 8.uzdevums
x = 3.1415926
y = -12.9999
print("\nSākuma skaitlis x: ", x)
print("Noapaļots skaitlis bez decimāldaļām x: "+"{:.0f}".format(x));
print("Sākuma skaitlis y: ", y)
print("Noapaļots skaitlis bez decimāldaļām y: "+"{:.0f}".format(y));
print(" ")

# 9.uzdevums
c = str(input('Ievadi vārdu: '))
pirmais = c[0]
c = c.lower()
c = c[::-1]
c = c.capitalize()
print(c+". Pamatīgs juceklis, vai ne,",pirmais + "?")