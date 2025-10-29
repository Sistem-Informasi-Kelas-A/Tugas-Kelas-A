angka = int(input("Masukkan sebuah angka: "))

adalah_genap = angka % 2 == 0
adalah_ganjil = not adalah_genap
print("Angka", angka, "adalah genap:", adalah_genap)
print("Angka", angka, "adalah ganjil:", adalah_ganjil)