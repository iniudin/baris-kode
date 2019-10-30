def nilai_mutlak(bilangan):
	if bilangan < 0:
		bilangan = -bilangan
	return bilangan

def manhattan(x1, x2, y1, y2):
	absis = x1 - x2
	ordinat = y1 - y2
	hasil = nilai_mutlak(absis) + nilai_mutlak(ordinat)
	return hasil

x1 = int(input("Masukan absis x1: "))
y1 = int(input("Masukan ordinat y1: "))
x2 = int(input("Masukan absis x2: "))
y2 = int(input("Masukan ordinat y2: "))

jarak = manhattan(x1, x2, y1, y2)
print(f"Jarak Manhattan adalah {jarak} satuan.")
