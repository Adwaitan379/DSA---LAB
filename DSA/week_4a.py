def quicksort(arr,low,high):
    if low<high:
        pivot = low
        i = low
        j = high
        while i<j:
            while arr[i]<=arr[pivot] and i<j:
                i+=1
            while arr[j]>arr[pivot]:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[j],arr[pivot] = arr[pivot],arr[j]
        quicksort(arr,low,j-1)
        quicksort(arr,j+1,high)
n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter value:"))
    arr.append(num)
quicksort(arr,0,n-1)
print(arr)

