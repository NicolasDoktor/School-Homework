word = "valorant"
g_letters = []
lives = 8


while True:
    display = ""
    for letter in word:
        if letter in g_letters:
            display += letter
        else:
            display += " "
    print("\nslovo:", display)
    print("životy:", lives)
    
    guess = input("hádej písmeno: ")
    
    if guess in g_letters:
        print("tohle písmeno jsi už uhádl")
        continue
    
    g_letters.append(guess)
    
    if guess not in word:
        print("špatně")
        lives -= 1
        if lives == 0:
            print("konec hry. Slovo bylo:", word)
            break
    else:
        print("správně")
        if all(letter in g_letters for letter in word):
            print("vyhral jsi, slovo je:", word)
            break
