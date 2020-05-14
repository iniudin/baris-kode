data1 = [1, 3, 6, 7, 10]
data2 = [2, 5, 8, 11, 14]

multipler = int(input())

dijumlah = output = [x + y for x, y in zip(data1, data2)]

result = [i * multipler for i in dijumlah]
print(result)