def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter value:"))
    arr.append(num)
bubbleSort(arr)
print(arr)
