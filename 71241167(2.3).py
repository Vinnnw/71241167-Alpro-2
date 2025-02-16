gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_kerja_per_minggu = int(input("Masukkan jumlah jam kerja per minggu: "))

pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja_per_minggu * 5
pendapatan_setelah_pajak = pendapatan_sebelum_pajak * 0.86
pakaian_aksesoris = pendapatan_setelah_pajak * 0.10
alat_tulis = pendapatan_setelah_pajak * 0.01
sisa_uang = pendapatan_setelah_pajak - pakaian_aksesoris - alat_tulis
sedekah = sisa_uang * 0.25
anak_yatim = sedekah * 0.30
kaum_dhuafa = sedekah - anak_yatim

# Output hasil
print("\nHasil perhitungan:")
print("Pendapatan Budi sebelum pajak: Rp", round(pendapatan_sebelum_pajak, 2))
print("Pendapatan Budi setelah pajak: Rp", round(pendapatan_setelah_pajak, 2))
print("Uang untuk pakaian dan aksesoris: Rp", round(pakaian_aksesoris, 2))
print("Uang untuk alat tulis: Rp", round(alat_tulis, 2))
print("Uang yang akan disedekahkan: Rp", round(sedekah, 2))
print("Uang untuk anak yatim: Rp", round(anak_yatim, 2))
print("Uang untuk kaum dhuafa: Rp", round(kaum_dhuafa, 2))
