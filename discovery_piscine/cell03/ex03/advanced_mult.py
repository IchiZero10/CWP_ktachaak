for i in range(11):
    print(f"Table de {i}:",*(f"{i*j}" for j in range(11)))