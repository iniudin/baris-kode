"""
Goal: 
 Membuat program peritungan tabungan
 input: tahun
 ouput: jumlah tabungan tiap bulan dan tahun.
"""

# Preparation
tahun : int
bulan : int = 12
# Diasumsikan sebulan ada 4 minggu
minggu : int = 4

# Setoran tetap adalah Rp 50.000
setoran : int = 50000
# Mula-mula tabungan adalah 0
tabungan = 0

tahun = int(input("Masukkan jangka kamu menabung (tahun): "))

# Looping 1, adalah lama user menabung (dlm tahun).
for thn in range(1, tahun+1):
    # Looping 2, untuk menampilkan tabungan per bulan.
    for bln in range(1, bulan+1):
        # Looping 3, menambahkan tabungan dari setoran.
        for _ in range(minggu):
            tabungan += setoran
        print(f"- Bulan ke {bln} adalah Rp {tabungan}")
    print(f"Tabungan tahun ke {thn} adalah Rp {tabungan}")
