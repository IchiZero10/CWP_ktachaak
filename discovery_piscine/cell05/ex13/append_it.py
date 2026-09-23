import sys

if len(sys.argv) <= 1:
    print("none")
else:
    for i in sys.argv[1:]:
        print(i if i.endswith("ism") else i + "ism")
