import sys
print(("Good job!" if input("What was the parameter? ")==sys.argv[1] else "Nope, sorry...") if len(sys.argv) ==2 else "none")