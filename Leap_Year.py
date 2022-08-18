a = int(input("Enter the Year :\n"))
if(a%400==0 and a%100==0) or (a%100!=0 and a%4==0):
    print(f"{a} is leap Year:\n")
else:
    print(f"{a} is not leap Year:\n")
