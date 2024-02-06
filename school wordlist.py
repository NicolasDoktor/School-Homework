arr = [["s","p","g","y"],
       ["t","f","r","q"],
       ["a","h","o","t"],
       ["n","b","s","l"]]
word = "python"
sum = 0

for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] == word[0]:
            print(f"{word[0]} je na {x,y}")
            if sum != len(word):
                sum += 1
