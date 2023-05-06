###Suma elementelor din lista prin loop (fara recursie)
##def sum(arr):
## total = 0
## for x in arr:
##  total += x
## return total
##print (sum([100,200,64, 2, 3, 4]))

def suma(arr):
    if arr==[]:       # <=> len(arr)==0
        return 0
    return arr[0]+suma(arr[1:])

print (suma([100,200,64, 2, 3, 4]))

###Numar cate elemente sunt in lista
##def count(arr):
##    if len(arr)==0:    # <=> arr==[]
##        return 0
##    return 1+count(arr[1:])
##
##print (count([100,200,64, 2, 3, 4]))            
