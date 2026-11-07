def compound(power,n):
    if n==1:
        return power
    return power*compound(power,n-1)

n = int(input("Enter number of years:"))
p = int(input("Enter principle growth:"))
res =  compound(p,n)
print(res)
