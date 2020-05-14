inputan = int(input())
pembagi = int(input())
ganjil = list()
genap = list()

num = 1
while True:
    if num % 2 == 0:
        genap.append(num)
    else:
        ganjil.append(num)
    num += 1
    
    if len(genap) == inputan and len(ganjil) == inputan:
        break


for i in range(len(genap)):
    genap[i] = genap[i] / pembagi
    ganjil[i] = ganjil[i] / pembagi

output = [x + y for x, y in zip(ganjil, genap)]

print(output)