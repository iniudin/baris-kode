def main():
	# Deklarasi Variable
	user_input : int
	# variable inputan menampung semua inputan dari user.
	inputan : list = []
	jumlah: int
	rerata : int
	nilai_terkecil : int
	nilai_terbesar : int
	
	# program akan berjalan secara terus menerus
	while True:
		user_input = int(input())
		if user_input != -1:
			inputan.append(user_input)
		else:
			break
	# Proses total dari inputan dengan menggunakan fungsi sum()
	jumlah = sum(inputan)
	# Rerata jumlah / sebanyak inputan
	rerata = jumlah / len(inputan)
	# mengambil nilai terkecil dengan fungsi min()
	nilai_terkecil = min(inputan)
	# mengambil nilai terbesar dengan fungsi max()
	nilai_terbesar = max(inputan)
	
	# Menampilkan hasil penghitungan
	print(f"Jumlah: {jumlah}")
	print(f"Rata-rata: {rerata}")
	print(f"Nilai terkecil: {nilai_terkecil}")
	print(f"Nilai terbesar: {nilai_terbesar}")

if __name__ == "__main__":
	main()