import sys
if len(sys.argv) <= 3:
    print("none")
else:
    print(*([sys.argv[i] for i in range(len(sys.argv) - 1, 0, -1)]))
