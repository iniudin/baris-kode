# import time
def main():
	# Deklarasi variabel
	angka = input()
	angka_2 = angka
	angka_3 = 1
	while True:
		# dicasting menjadi str agar bisa diiterasikan
		for i in str(angka_2):
			angka_3 *= int(i)
		# print(angka_2)
		if (len(str(angka_3))) == 1:
			print(f"Hasil: {angka_3}")
			break
		angka_2 = angka_3
		angka_3 = 1
		# time.sleep(1)
if __name__ == '__main__':
	main()