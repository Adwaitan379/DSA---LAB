def binarySearch(arr,key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==key:
            return mid
        if key<arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1
n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter value:"))
    arr.append(num)
val = int(input("Enter number to search:"))
arr.sort()
res = binarySearch(arr,val)
if res!=-1:
    print("Element found at the index:",res)
else:
    print("Element not found")
