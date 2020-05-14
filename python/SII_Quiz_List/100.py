multipler = int(input())
data = [1, 3, 5, 7, 9, 11, 13, 15]

for i, v in enumerate(data):
	if i == 2 or i == 5:
		data[i] = data[i] * multipler
print(data)