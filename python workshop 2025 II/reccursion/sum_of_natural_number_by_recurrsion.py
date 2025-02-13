def sum_n(n):
    if(n==1):
        return 1
    else:
        return n+sum_n(n-1)
a=int(input("Enter value of n:"))
sum=sum_n(a)
print(sum)

