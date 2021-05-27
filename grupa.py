
#1
def vards(s):
    ret = ""
    i = True  
    for mama in s:
        if i:
            ret += mama.upper()
        else:
            ret += mama.lower()
        if mama != ' ':
            i = not i
    return ret
print(vards("ieraksts"))


#2
st= "Izdrukā visus vārdus, kas sākas ar v burtu"
for i in st.split():
    if i.startswith("v"):
        print(i)


#3
def animal_crackers(string):
    s1, s2 = string.split(' ')
    return s1[0].upper() == s2[0].upper()
print(animal_crackers("Balts mbalodis"))



#4
def front_back(str):
    if len(str)  < 2:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

print(front_back("balts"))


#5
def summa(a): 
    sum = 0
    for sk in str(a):
        sum += int(sk)
    return sum

a = 720
print(summa(a))