def print_field(field):
    for x in field:
        print(" ".join(x))

def check(field, player):
   # s tímhle my pomohl kamarád
    for i in range(3):
        if all(field[i][j] == player for j in range(3)) or all(field[j][i] == player for j in range(3)):
            return True
    
    if all(field[i][i] == player for i in range(3)) or all(field[i][2-i] == player for i in range(3)):
        return True
    return False

field = [["_" for _ in range(3)] for _ in range(3)]
current_player = 0

def take_turn():
    global current_player
    play_x = int(input("vložte x : "))
    play_y = int(input("vložte y : "))
    
    if play_x > 2 or play_y > 2:
        print("moc velké číslo")
        return
    
    if field[play_y][play_x] != "_":
        print("tato pozice je už zabraná")
        return
    
    if current_player == 0:
        field[play_y][play_x] = "X"
        current_player = 1
    else:
        field[play_y][play_x] = "O"
        current_player = 0

print("Vítej ve hře")
print_field(field)

while True:
    take_turn()
    print_field(field)
    