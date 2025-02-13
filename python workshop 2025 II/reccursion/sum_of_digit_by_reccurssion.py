# This program is used to find the sum of digits of a number using reccurssion.
def sum_n(n):
    if n==0:
        return 0
    else:
        return n%10+sum_n(n//10)
n=int(input("Enter the number:"))
print(sum_n(n))