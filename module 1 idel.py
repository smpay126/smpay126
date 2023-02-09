def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial


n = int(input("enter number 'n' to get factorial: "))
print("the factorial of ",n,"is",fact(n))
