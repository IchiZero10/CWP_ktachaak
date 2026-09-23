import sys
def downcase_it(str:str):
    return str.lower()
if len(sys.argv) >1:
    print(*[downcase_it(i) for i in sys.argv[1:]],sep="\n")
else:
    print("none")