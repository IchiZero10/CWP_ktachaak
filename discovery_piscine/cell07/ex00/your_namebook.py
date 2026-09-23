persons = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}
print([" ".join(j.title() for j in i) for i in persons.items()])