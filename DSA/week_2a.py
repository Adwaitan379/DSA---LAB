def linearSearch(arr,val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

n = int(input("Enter no of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter value:"))
    arr.append(num)
val = int(input("Enter number to search:"))
res = linearSearch(arr,val)
if res!=-1:
    print("Element found at the index:",res)
else:
    print("Element not found")
