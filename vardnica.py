tel = {"direktors": "911", "vietnieks": "112", "mamma": "99999999"}
print(tel["direktors"])
cenas = {"piens": 1.22, "banāni": 0.94}
print(cenas["piens"])
d = {"k1": 123, "k2": [10, 11, 12], "k3": {"atsl1": 100}}
#vāŗdnīcas var uzglabāt dazādus datu tipus, tai skaitā list un vārdnīcas
print(d["k2"])
print(d["k3"])
print(d["k2"][2])  #izdrukā elementu ar noradīto indeksu un atslegu.
print(d["k3"]["atsl1"])  #izdrukā ligzdvārdu elementus

d = {"k1": "vertiba", "k2": [10, 11, 12], "k3": {"atsl1": 100, "atsl2": 200}}
#vāŗdnīcas var uzglabāt dazādus datu tipus, tai skaitā list un vārdnīcas
print(d["k1"])
print(d["k2"])
print(d["k2"][2])  #izdrukā elementu ar noradīto indeksu un atslegu.
print(d["k3"]["atsl1"])  #izdrukā ligzdvārdu elementus
print(d["k2"][1])

my_dict = {'key1': ['a', 'b', 'c']}
print(my_dict)
my_list = my_dict['key1']
print(my_list)
burts = my_list[2]
print(burts)
print(burts.upper())#izdruka lielo C, kas atrodas vardnicas vertiba
print(my_dict ['key1'] [2].upper())
#viena rinda atlasa elementu un parveido

new_dict={"k1":100, "k2":200}
print(new_dict)
new_dict["k3"]=300
print(new_dict)
new_dict["k1"]="simts"
print(new_dict)

print(new_dict.keys())
print(new_dict.values())
vertibu_list = list(new_dict.values())
print(vertibu_list)
print(new_dict.items())
print(new_dict.get("k1"))
print(new_dict.pop("k1"))
print(new_dict.update())
print(new_dict)


