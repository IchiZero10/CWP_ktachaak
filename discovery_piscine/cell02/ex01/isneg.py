inp = int(input())
print(
    "This number is positive."
    if inp > 0
    else (
        "This number is negative."
        if inp < 0
        else "This number is both positive and negative."
    )
)
