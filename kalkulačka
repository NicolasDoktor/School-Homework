def sčítání(x, y):
    return x + y
#sečte dvě proměné
def odčítání(x, y):
    return x - y
#odečte 2 proměné
def násobení(x, y):
    return x * y
# znásobí 2 proměné
def dělení(x, y):
    return x / y
#vydělí 2 proměné
def vstup():
    x = int(input("Zadejte první číslo: "))
    y = int(input("Zadejte druhé číslo: "))
    return x,y

def result(výsledek):
    print("Výsledek:", výsledek)
#vypíše to výsledek
def program():
    x,y = vstup()
    operace = input("Zadejte operaci (+, -, *, /): ")
    if operace == "+":
        výsledek = sčítání(x,y)
    elif operace == "-":
        výsledek = odčítání(x,y)
    elif operace == "*":
        výsledek = násobení(x,y)
    elif operace == "/":
        výsledek = dělení(x,y)
    else:
        print("Neplatná operace.")
        return
    result(výsledek)

if __name__ == '__main__':
    program()
#spouští to celý program