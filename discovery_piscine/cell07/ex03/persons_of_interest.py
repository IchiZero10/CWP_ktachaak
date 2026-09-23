def famous_births(dic:dict):
    val = sorted(list(dic.values()),key=lambda x:x["date_of_birth"])
    print(*[f"{v["name"]} is a great scientist born in {v["date_of_birth"]}." for v in val],sep="\n")


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)