def romawi(angka):
	angka = int(input("Masukan angka: "))

	if angka > 0 and angka <= 3:
	    hasil = "I" * angka
	elif angka >= 5 and angka <= 8:
	    hasil = f"V{'I' * (angka - 5)}" 
	elif angka == 4:
	    hasil = "IV"
	elif angka >= 9 or angka == 10:
	    hasil = f"{'I' * (10-angka)}X"
	else:
	    hasil = "Hanya mencakup 1 - 10" 
	return hasil

print(romawi(9))
