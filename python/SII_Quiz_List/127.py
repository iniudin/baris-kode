data = [1, 3, 6, 7, 10, 11, 17, 20, 23, 36]
new_data = list()
inputan = int(input())

if inputan > 35:
	exit()
for i in data:
	if i > inputan:
		new_data.append(i)
print(new_data)