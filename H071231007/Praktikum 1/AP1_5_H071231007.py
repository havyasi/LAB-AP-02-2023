#progaram konversi waktu dari detik ke jam:menit:detik
print("Konversi detik ke jam")
z = int(input("Masukkan jumlah detik : "))

jam = z // 3600
z %= 3600
menit = z // 60
z %= 60
detik = z % 60

print(f"{jam:03d}:{menit:03d}:{detik:03d}")
