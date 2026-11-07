def search(arr,i,val):
    if i>len(arr):
        return -1
    if arr[i]==val:
        return i
    else:
        return search(arr,i+1,val)
n = int(input("Enter size of an array:"))
arr = []
for i in range(n):
    num = int(input("Enter Id:"))
    arr.append(num)
val = int(input("Enter Id to search:"))
res = search(arr,0,val)
if res != -1:
    print("Id found at index:",res)
else:
    print("Id Not found")
    
