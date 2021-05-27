def myfunc(a, b):
    return sum((a, b))*0.05

print(myfunc(40, 60))

def myfunc2(*args):
    return sum(args)*0.05

print(myfunc2(40, 60, 100))


def myfuncKW(**kwargs):
    if "auglis" in kwargs:
        print(f"Mana izvēle ir {kwargs ['auglis']}.")
    else:
        print("Nevienu augli neatrodu.")


myfuncKW(auglis="ābols", dārzenis="burkāns")
