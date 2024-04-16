slovník = {
        "name": "jméno",
        "age": "věk",
        "apple": "jablko" 
        }

while True:
    user_input = input("zadej anglické slovo: ")
    if user_input in slovník:
        print(slovník[user_input])
    else:
        add_word_pompt = input("chceš přidat překlad? y/n: ")
        if add_word_pompt == "y":
            add_word = input(f"zadej překlad slova {user_input}: ")
            slovník[user_input] = add_word
        else:
            continue
        
