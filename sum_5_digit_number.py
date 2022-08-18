a = int(input("enter the 5 digit number:\n"))
s = 0
while a > 0:
    r = int(a % 10)
    s = s+r
    a = int(a/10)
print(f"Sum of digits are : {s} \n")




