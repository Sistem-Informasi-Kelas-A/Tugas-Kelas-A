status_member = input("Apakah Anda seorang member? (ya/tidak): ").strip().lower()
total_belanja = int(input("Masukkan total belanja Anda: "))
dapat_diskon = status_member == "ya" and total_belanja > 500000

print("Dapat diskon:", dapat_diskon)