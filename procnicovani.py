#print("Vítej ve hře random generátor vtipných jmen")

#name = input("zadej své jméno: ")
#vlastnost = input("zadej jaká je tvoje typická vlastnost? : ")

#print(name + " " + vlastnost)


age = 30
years = 90 - age
months = years * 12
weeks = years * 52
days = years * 365

print(f"zbývá ti {years} let, \n {months} měsíců, \n {weeks} týdnů, \n {days} dní, \n")


field = [["_" for _ in range(3)] for _ in range(3)] # Vytvoření herního pole

def print_field(field): # Funkce pro vypsání herního pole
    for x in field:
        print(" ".join(x))

current_player = 0

while True: # Nekonečná herní smyčka
    print_field(field) # Vypíše herní pole na začátku každého kola
    if current_player == 0: # Vypíše, jaký hráč je na řadě
        print("hraje hráč X")
    else:
        print("hraje hráč O")

    play_x = input("zadej x:") # Uloží souřadnici x
    if play_x == "q": # Ukončí hru, pokud místo souřadnice x bylo napsáno "q"
        break
    play_x = int(play_x)
    play_y = int(input("zadej y:")) # Uloží souřadnici y
    if play_x or play_y > 2:
        print("moc velké číslo")
        
def take_turn():
    if current_player == 0: # Zjišťuje, jaký hráč je na řadě a podle toho vypisuje buď "x" nebo "o"
        field[play_y][play_x] = "x"
        current_player = 1
    else:
        field[play_y][play_x] = "o"
        current_player = 0
    if field != "_":
        print("tohle místo je už zabrané")