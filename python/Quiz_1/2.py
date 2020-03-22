def main():
	# Deklarasi Variable
	batas_awal : int
	batas_akhir : int

	batas_awal = int(input())
	batas_akhir = int(input())
	
	# Agar 1, tidak dianggap bilangan prima maka diubah menjadi 2
	if batas_awal == 1:
		batas_awal = 2
	for i in range(batas_awal, batas_akhir):
		for x in range(2, i):
			if i % x == 0:
				break;
		else:
			print(i, end=" ")
if __name__ == "__main__":
	main()