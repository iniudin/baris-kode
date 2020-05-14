def adder(n, data1, data2):
	result = data1[n] * data2[n]
	return result

data1 = [1, 3, 6, 7, 10]
data2 = [2, 5, 8, 11, 14]

inputan = int(input())

if inputan >= 0 and inputan <= 4:
	print(adder(n=inputan, data1=data1, data2=data2))
