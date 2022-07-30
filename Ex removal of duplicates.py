def dupdup(listie):
    for i in listie:
        listie.remove(i)
        return listie

print(dupdup([11,22,33,44,11]))        