# Faktor bilangan bulat dari X
N = int(input("Input bilangan bulat: "))
pembagi = N
while pembagi>0:
    sisa = N % pembagi
    if sisa == 0:
        print(pembagi)
    pembagi-=1
