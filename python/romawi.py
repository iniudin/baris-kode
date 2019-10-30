def romawi(angka):
	roma = {
		'I': 1,
		'IV': 4,
		'V': 5,
		'IX': 9,
		'X': 10,
		'XL': 40,
		'L':50,
		'XC': 90,
		'C': 100,
		'CD': 400,
		'D':500,
		'CM': 900,
		'M':1000
	}

	range_flag = None
	for roman, integer in roma.items():
		if integer == angka:
			return roman
		if angka > integer:
			range_flag = roman
	temp = angka - roma[range_flag]
	return range_flag + romawi(temp)
bilangan = int(input("Masukan angka arab:"))

print(f"Angka romawi dari {bilangan} adalah {romawi(bilangan)}")
