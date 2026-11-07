def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter value:"))
    arr.append(num)
insertionSort(arr)
print(arr)
