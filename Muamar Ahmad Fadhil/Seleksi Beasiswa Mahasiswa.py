ipk = float(input("Masukkan IPK Anda: "))
pendapatan_ortu = int(input("Masukkan pendapat orang tua Anda : "))
lolos_seleksi = ipk == 4.0 or pendapatan_ortu < 1500000

print("Lolos seleksi beasiswa:", lolos_seleksi)