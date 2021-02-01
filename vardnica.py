tel = {"direktors" : "911", "vietnieks" : "112", "mamma" : "99999999"}
print(tel["direktors"])
cenas={"piens": 1.22, "banāni": 0.94}
print(cenas["piens"])
d = {"k1": 123, "k2":[10,11,12], "k3":{"atsl1": 100}}
#vāŗdnīcas var uzglabāt dazādus datu tipus, tai skaitā list un vārdnīcas
print(d["k2"])
print(d["k3"])
print(d["k2"][2]) #izdrukā elementu ar noradīto indeksu un atslegu.
print(d["k3"]["atsl1"]) #izdrukā ligzdvārdu elementus

d = {"k1": "vertiba", "k2": [10, 11, 12], "k3":{"atsl1": 100, "atsl2": 200}}
#vāŗdnīcas var uzglabāt dazādus datu tipus, tai skaitā list un vārdnīcas
print(d["k1"])
print(d["k2"])
print(d["k2"][2])  #izdrukā elementu ar noradīto indeksu un atslegu.
print(d["k3"]["atsl1"])  #izdrukā ligzdvārdu elementus
print(d["k2"][1])