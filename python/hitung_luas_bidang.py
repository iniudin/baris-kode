"""
    Nama: Ahmad Syaifudin
    NIM: 192410103093
    Program: Perhitungan luas suatu bangun.
    Source: https://github.com/sysfdn/baris-kode/edit/master/python/hitung_luas_bidang.py
"""

# Preparation
# nama_variabel: tipe data = nilai
choose: str = ""
luas: float = 0
panjang: float = 0
lebar: float = 0
alas: float = 0
tinggi: float = 0
PHI: float = 3.14
jari_jari: float = 0
is_done: bool = False

# Ketika nilai variable is_done adalah False maka program akan berjalan, jika tidak maka akan berhenti.
while is_done is not True:
    # Menampilkan daftar menu pilihan
    print("=== Program Penghitung Luas === "
    	"\nDaftar Bidang: ",
    	"\n1> Segiempat",
    	"\n2> Segitiga",
    	"\n3> Lingkaran",
    	"\n0> Keluar"
    )
    # User menginputkan pilihannya, dalam bentuk str
    choose = input("Pilih Menu> ")
    if choose == "1":
        # Ketika user memilih nomor 1, maka program akan menampilkan menu menghitung luas Segiempat.
        print("Menghitung Luas Segiempat")
        # Program meminta user untuk menginputkan panjang dan lebar sisi bangun.
        panjang = float(input("Input nilai sisi panjang (cm): "))
        lebar = float(input("Input nilai sisi lebar (cm): "))
        # Program memproses perhitungan
        luas = panjang * lebar
        # Program Menampilkan hasil hitung
        print("Hasil hitung luas Segiempat: ", luas)
    elif choose == "2":
        # Ketika user memilih nomor 2, maka program akan menampilkan menu menghitung luas segitiga.
        print("Menghitung Luas Segitiga")
        # Program meminta user untuk menginputkan alas dan tinggi sisi bangun.
        alas = float(input("Input nilai sisi alas (cm): "))
        tinggi = float(input("Input nilai sisi tinggi (cm): "))
        # Program memproses perhitungan
        luas = 0.5 * alas * tinggi
        # Program Menampilkan hasil hitung
        print("Hasil hitung luas segitiga: ", luas)
    elif choose == "3":
        # Ketika user memilih nomor 3, maka program akan menampilkan menu menghitung luas lingkaran.
        print("Menghitung Luas Lingkaran")
        # Program meminta user untuk menginputkan jari-jari bangun.
        jari_jari = float(input("Input nilai jari-jari (cm): "))
        # Program memproses perhitungan
        luas = PHI * jari_jari**2
        # Program Menampilkan hasil hitung
        print("Hasil hitung luas Lingkaran: ", luas)
    elif choose == "0":
        # Ketika user memilih nomor o, maka program akan mengubah nilai variabel `is_done` menjadi True.
        print("Program berhenti, Bye!")
        is_done = True
    else:
        # Ketika user memilih menu/opsi yang salah maka program akan mentrigger user
        print("Kamu memilih Menu yang salah!")
    print()
