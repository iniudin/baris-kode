panjang_sawah = int(input("Masukan Panjang Sawah: "))
lebar_sawah = int(input("Masukan Lebar Sawah: "))
sekali_pupuk_kilo = int(input("Masukan Jumlah Pupuk / Kilo: "))

bangun = panjang_sawah * lebar_sawah
bibit = bangun / 0.04
pupuk_seminggu = bangun * 0.4
total_pupuk = pupuk_seminggu * 16
pupuk_kurang = pupuk_seminggu - sekali_pupuk_kilo
pupuk_lebih = sekali_pupuk_kilo - pupuk_seminggu

text = f"\nLuas sawah bapak: {bangun}"
text += f"\nBanyak bibit yang dibutuhkan: {bibit}"

if pupuk_seminggu == sekali_pupuk_kilo:
  text += f"\nPupuk anda Pas!"
elif pupuk_seminggu > sekali_pupuk_kilo:
  text += f"\nPupuk anda kurang: {pupuk_kurang} /kilo"
else:
  text += f"\nPupuk anda lebih: {pupuk_lebih} /kilo"
text += f"\nJumlah pupuk setiap minggunya: {pupuk_seminggu} /Kilo"
text += f"\nTotal Pupuk yang dibutuhkan: {total_pupuk} /Kilo"

print(text)
