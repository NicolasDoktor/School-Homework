height = int(input("zadej výšku: "))
weight = int(input("zadej váhu: "))

height /=100
bmi = weight/(height **2)

if bmi < 18.5:
    print("podváha")
elif bmi > 25:
    print("nadváha")
else:
    print("normální")
