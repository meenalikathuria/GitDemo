a = int(input("Enter the Number to reverse : \n"))
rev = 0
while a > 0:
    r = int(a % 10)
    rev = (rev * 10) + r
    a = int(a / 10)
print(f"Reverse = {rev} \n")
