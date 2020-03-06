# Preparation
choose: str = ""
luas: float = 0
panjang: float = 0
lebar: float = 0
alas: float = 0
tinggi: float = 0
PHI: float = 3.14
is_done: bool = False
while is_done == False:
    print("=== Program Penghitung Luas === ")
    print("Daftar Bidang: ")
    print("1> Segi Empat")
    print("2> Segi Tiga")
    print("3> Lingkaran")
    print("0> Keluar")
    choose = input("Pilih Menu> ")
    if choose == "1":
        print("Menghitung Luas Segi Empat")
        panjang = float(input("Input Panjang (cm): "))
        lebar = float(input("Input Lebar (cm): "))
        luas = panjang * lebar
        print("Hasil Luas Segi Empat: ", luas)
    elif choose == "2":
        print("Menghitung Luas Segi Tiga")
        alas = float(input("Input Alas (cm): "))
        tinggi = float(input("Input Tinggi (cm): "))
        luas = 0.5 * alas * tinggi
        print("Hasil Luas Segi Tiga: ", luas)
    elif choose == "3":
        print("Menghitung Luas Lingkaran")
        jari_jari = float(input("Input Jari-jari (cm): "))
        luas = PHI * jari_jari**2
        print("Hasil Luas Lingkaran: ", luas)
    elif choose == "0":
        print("Program berhenti, Terimakasih!")
        is_done = True
    else:
        print("Kamu memilih bidang yang salah")
    print()
