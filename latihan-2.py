nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
alamat = input("Masukkan Alamat: ")

data_diri = (nama, nim, alamat)

# Menampilkan data diri
print("NIM    : ", data_diri[1])
print("NAMA   : ", data_diri[0])
print("ALAMAT : ", data_diri[2])

# Memisahkan NIM menjadi tuple
nim_tuple = tuple(data_diri[1])
print("NIM: ", nim_tuple)

# Memisahkan nama depan menjadi tuple
nama_depan = tuple(data_diri[0].split()[0])
print("NAMA DEPAN: ", nama_depan)

# Membalikkan nama menjadi tuple
nama_terbalik = tuple(data_diri[0].split()[::-1])
print("NAMA TERBALIK: ", nama_terbalik)