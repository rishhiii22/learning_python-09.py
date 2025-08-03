a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

if(b == 0):
    raise ZeroDivisionError("Heyy our program does not support the value of b as zero but you have putted it so its an Error.")
else:
    print(f"The division a/b is {a/b}")

    