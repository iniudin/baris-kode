for baris in range(level):
    for kolom in range(level):
        if kolom == 0 or baris == 0:
            print("*", end=" ")
        elif baris == level-1 or kolom == level-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
