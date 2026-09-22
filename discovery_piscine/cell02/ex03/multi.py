inp1 = int(input("Enter the first number:"))
inp2 = int(input("Enter the second number:"))
result = inp1 * inp2
print(f"{inp1} x {inp2} = {result}")
print(
    "This number is positive."
    if result > 0
    else (
        "This number is negative."
        if result < 0
        else "This number is both positive and negative."
    )
)
