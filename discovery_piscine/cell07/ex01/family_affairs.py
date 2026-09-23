dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red",
}
def find_the_redheads(dic:dict):
    print([i[0] for i in dic.items() if i[1] == "red"])
find_the_redheads(dupont_family)