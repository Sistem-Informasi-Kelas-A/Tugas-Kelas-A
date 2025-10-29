level_akses = input("Masukkan level anda admin/teknisi/user: ").strip().lower()
jam_masuk = int(input("Masukkan jam masuk (0-23): "))
boleh_masuk = (level_akses == "admin") or (level_akses == "teknisi" and jam_masuk >= 9 and jam_masuk <= 17)
print("Boleh mengakses ruang server:", boleh_masuk)