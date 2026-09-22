inp = int(input("Enter a number\n"))
print(*(f"{i} x {inp} = {i*inp}" for i in range(10)),sep="\n")
