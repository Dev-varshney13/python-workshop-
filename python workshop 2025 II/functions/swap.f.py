#wap by using function to swap two numbers
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
n=int(input("Enter a number:"))
m=int(input("Enter another number:"))
n,m=swap(n,m)
print("After swapping the numbers are:",n,m)
