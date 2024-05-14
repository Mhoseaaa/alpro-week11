def menghitung_distribusi_email(filename):
    try:
        # Membuka file mbox
        mbox_file = open(filename, 'r')

        # Membaca setiap baris dalam file mbox
        lines = mbox_file.readlines()

        # Inisialisasi kamus untuk menyimpan distribusi jam
        distribution = {}

        # Menghitung distribusi jam
        for line in lines:
            if line.startswith('From '):
                words = line.split()
                time = words[5].split(':')[0]
                distribution[time] = distribution.get(time, 0) + 1

        # Menampilkan hasil distribusi jam
        for hour, count in sorted(distribution.items()):
            print(hour, count)

        # Menutup file mbox
        mbox_file.close()

    except FileNotFoundError:
        print("File not found.")

# Meminta pengguna untuk memasukkan nama file mbox
filename = input("Enter a file name: ")

# Memanggil fungsi untuk menghitung distribusi jam
menghitung_distribusi_email(filename)