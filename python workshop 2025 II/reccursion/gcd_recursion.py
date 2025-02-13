def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print(gcd(m,n))