##def quicksort(arr):  #quicksort cu pivot in mijloc
##    if len(arr)<2:
##        return arr
##    else:
##        pivot=arr[len(arr)//2]
##        less=[i for i in arr[0:len(arr)//2] if i <= pivot] + [i for i in arr[len(arr)//2+1:len(arr)] if i <= pivot] 
##        greater=[i for i in arr[0:len(arr)//2] if i > pivot] + [i for i in arr[len(arr)//2+1:len(arr)] if i > pivot]
##        return quicksort(less) + [pivot] + quicksort(greater)
##
##print (quicksort([10,2,3,4,7,1]))

def quicksort(arr):  #quicksort cu pivot in primul element din lista
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i <= pivot] 
        greater=[i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([10,2,3,4,7,1]))
