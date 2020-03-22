def main():
	
	level = int(input())

	for baris in range(level):
		for kolom in range(level):
			if kolom == 0 or baris == 0:
				print("*", end=" ")
			elif kolom == level-1 or baris == level-1:
				print("*", end=" ")
			# Garis miring kanan ke kiri
			elif kolom + baris == level-1:
				print("*", end=" ")
			# Garis miring kiri ke kanan
			elif kolom == baris:
				print("*", end=" ")
			else:
				print(" ", end=" ")
		print()
if __name__ == "__main__":
	main()