import sys
def shrink(string:str):
    return string[:8]
def enlarge(string:str):
    return string + "Z"*(8-len(string))
def main():
    if len(sys.argv) <=1:
        print("none")
    else:
        for i in sys.argv[1:]:
            if len(i) > 8:
                print(shrink(i))
            elif len(i) < 8:
                print(enlarge(i))
            else:
                print(i)
main()