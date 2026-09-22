inp = int(input("Enter a number less that 25\n"))
print(*(f"Inside the loop, my variable is {i}\n" for i in range(inp,26)) if inp <25 else "Error",sep="")