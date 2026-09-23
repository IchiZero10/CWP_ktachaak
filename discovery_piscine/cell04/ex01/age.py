age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
nextyear = 10
for _ in range(3):
    print(f"In {nextyear} years, you'll be {age+10} years old.")
    nextyear += 10
    age += 10