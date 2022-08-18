a1 = int(input("Enter the first Number: "))
a2 = int(input("Enter the Second Number: "))

choice = int(input('''Press 1 for Sum of provided numbers
                      Press 2 for Subtraction of provided numbers
Press 3 for Multiply of provided numbers
Press 4 for Division of provided numbers
Press 5 for Remainder of provided numbers'''))

if choice==1:
    s = a1+a2
    print(f"Sum of {a1} and {a2} is {s}")
elif choice==2:
    sub = a1 - a2
    print(f"Subtraction of {a1} and {a2} is {sub}")
elif choice==3:
    m=a1*a2
    print(f"Multiply of {a1} and {a2} is {m}")
elif choice==4:
    d=a1/a2
    print(f"Division of {a1} and {a2} is {d}")
elif choice==5:
    r=a1%a2
    print(f"Remainder of {a1} and {a2} is {r}")
else:
    print("Invalid choice")