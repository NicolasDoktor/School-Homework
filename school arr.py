arr = [[23,58,41,69,32],[95,45,32,14,75],[52,61,85,12,8]]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        if arr[x][y] > 50:
    
            print(f"arr[{x}][{y}] = {arr[x][y]}")
          #vypíše čísla v poli která jsou větší než 50 i jejich indexy
