#wap to convert time in minutes using function
def minute(hour,mint):
    return (int(hour) * 60 + int(mint))
time=input("Enter the time in the format hh:mm: ")
hour,mint=time.split(":")
a=minute(hour,mint)
print(f"The time in minutes is: {a}")

