# Data Awal
saldo_awal = 5000000
pemasukan_bulanan = 7500000
pengeluaran_tetap = 4500000
investasi_bulanan = 1000000

# TODO 1: Hitung saldo setelah pemasukan dan pengeluaran
# Gunakan operator aritmatika dasar
saldo_setelah_transaksi = saldo_awal + pemasukan_bulanan - pengeluaran_tetap
print("Saldo setelah transaksi:", saldo_setelah_transaksi)

# TODO 2: Hitung total investasi setelah 6 bulan dengan bunga 5%
# Gunakan operator penugasan dan aritmatika
investasi_6_bulan = investasi_bulanan * 6 # Ini baru total pokok investasi
investasi_6_bulan += (investasi_6_bulan * 0.05) # ini tuh total pokok ditambah bunga 5%
print("Total investasi 6 bulan (termasuk bunga 5%):", investasi_6_bulan)

# TODO 3: Hitung persentase tabungan dari pemasukan
# Gunakan operator modulus dan pembagian
total_tabungan = pemasukan_bulanan - pengeluaran_tetap
persentase_tabungan = (total_tabungan / pemasukan_bulanan) * 100
print("Persentase tabungan dari pemasukan :", persentase_tabungan, "%")

# TODO 4: Prediksi saldo setelah 1 tahun dengan asumsi sama
# Gunakan operator penugasan majemuk
saldo_1_tahun = saldo_awal
# your code here - update saldo_1_tahun selama 12 bulan
sisa_tunai_bulanan = pemasukan_bulanan - pengeluaran_tetap - investasi_bulanan

for bulan in range(12):
    saldo_1_tahun += sisa_tunai_bulanan

print("jadi ini prediksi tabungan selama 1 tahun:", saldo_1_tahun)