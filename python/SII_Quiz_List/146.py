x = [2, 2, 3, 4, 5, 5, 5, 6, 6, 7]

inputan = int(input()) 
# Solve 1
print(x.count(inputan))
# Solve 2 
hasil = 0
for i in x:
	if i == inputan:
		hasil+=1
print(hasil)
