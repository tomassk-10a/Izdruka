
vards = input("Kā tevi sauc? ")
print(f"Labdien, {vards}.")

gadi = int(input("Cik tev gadu? "))

print("Tavs dzimšanas gads ir " + str(2021 - gadi))
print(f"Tavs dzimšanas gads ir {2021-gadi}")

celsijs = int(input("Raksti celsiju šeit: "))
print(f"Sanāks tik fārinheiti: {celsijs*9/5+32} ")

platums = int(input("Raksti platumu šeit: "))
augstums = int(input("Raksti audstumu šeit: "))
garums = int(input("Raksti garumu šeit: "))
print(f"Sanāks tāds tilpums: {platums*augstums*garums} ")

print("sveika \tpasaule")
print("sveika \npasaule")
print(len("tomass"))
print(len("! "))  #atstarpes un zimes

myString = "Kokonut!"
print(myString)
print(myString[2])
print(myString[-1])

myString = "abcdefghijklmnoprstuvz"
print(myString)
print(myString[2])
print(myString[2:])
print(myString[:2])
print(myString[0:3])
print(myString[::])
print(myString[::2])
print(myString[2:7:2])
print(myString[::-1])
