def pembulatan(bilangan):
    dibelakang_koma = bilangan * 10 - (bilangan * 10 // 1)

    if dibelakang_koma >= 0.5:
        hasil = ((bilangan * 10 + 1) // 1) / 10
    else:
        hasil = (bilangan * 10 // 1) / 10
    return hasil

print("Pembulatan Angka Desimal")
angka = float(input("Masukan bilangan desimal: "))
print(f"Hasil pembulatan dari {angka}, adalah {pembulatan(angka)}")
