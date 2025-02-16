tinggi = float(input("Masukkan tinggi badan (meter): "))
bmi = float(input("Masukkan BMI yang anda harapkan: "))

berat_badan = bmi * (tinggi ** 2)

print("Berat badan yang diperlukan untuk BMI", bmi, "adalah", round(berat_badan, 2), "kg.")
