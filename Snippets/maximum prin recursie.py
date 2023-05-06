def maxim(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maxim(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maxim([1,3,373,13,23,5]))
