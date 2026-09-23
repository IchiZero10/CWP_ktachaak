inp = float(input("Give me a number: "))
print(f"This number is a{"n integer." if inp.is_integer() else " decimal."}")