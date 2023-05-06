def selection_sort(arr):
    for i in range (len(arr)):
        min_index=i
        for j in range (i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
arr=[5,3,6,2,10,12,1,13,30]
selection_sort(arr)
print(arr)

#####Exemplu din internet
##A = [5,3,6,2,10,1,30]
##for i in range(len(A)):
##    min_idx = i
##    for j in range(i+1, len(A)):
##        if A[min_idx] > A[j]:
##            min_idx = j      
##    A[i], A[min_idx] = A[min_idx], A[i]
## 
##print ("Sorted array")
##print(A)

#####Exemplu din carte
##def find_smallest(arr):
##    smallest=arr[0]
##    smallest_index=0
##    for i in range (1,len(arr)):
##        if arr[i] < smallest:
##            smallest = arr[i]
##            smallest_index=i
##    return smallest_index
##
##def selection_sort(arr):
##    newArr=[]
##    for i in range (len(arr)):
##        small = find_smallest(arr)
##        newArr.append(arr.pop(small))
##    return newArr
##arr=[5,3,6,2,10,12,13,30]
##print (selection_sort(arr))
