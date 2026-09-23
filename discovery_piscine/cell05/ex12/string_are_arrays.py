import sys
counter = 0 if len(sys.argv) != 2 else sys.argv[1].lower().count("z")
print("z"*counter if counter else "none")