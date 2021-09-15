piemers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
from random import shuffle

shuffle(piemers)
print(piemers)
print()


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


"""
rezult = shuffle_list ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(rezult)
"""
mylist = [" ", "o", " "]
print(shuffle_list(mylist))
print()


def mans_minejums():
    minejums = ""
    while minejums not in ["0", "1", "2"]:
        minejums = input("Izvelies 1 vai 2 vai 0: ")
    return int(minejums)
mans_minejums()