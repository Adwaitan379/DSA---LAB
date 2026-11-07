def Launch(n):
    if n==0:
        print("Launch")
        return
    print(n)
    return Launch(n-1)

n = int(input("Enter Countdown:"))
Launch(n)
