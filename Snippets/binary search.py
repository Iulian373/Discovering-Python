def binary_search(lista, item):
    low=0
    high=len(lista)-1

    while low <= high:
        mid=(low+high)//2
        guess=lista[mid]
        if guess == item:
            return mid
        else:
         if guess > item:
            high=mid-1
         else :
            low=mid+1
    return None

my_list = [0,1,2,3,4,5,6,7,8,9,10]

print (binary_search(my_list,3))
print (binary_search(my_list, 13))
