import sys
if len(sys.argv) == 3:
    print(sys.argv[2].count(sys.argv[1]) or "none")
else:
    print("none")