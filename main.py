# Function tampilkan data
def tampilkan_data():
    print("Data mahasiswa")


# Function tambah data
def tambah_data():
    print("Tambah data")


# Function ubah data
def ubah_data():
    print("Ubah data")


# Function hapus data
def hapus_data():
    print("Hapus data")

# Program utama
while True:
    print("=================================================================")
    print("Program sederhana data mahasiswa powerd by : Mohamad Ridho Sunami")
    print("===========================================================")
    print("     DATA MAHASISWA ILMU KOMPUTER ANGKATAN 26              ")
    print("===========================================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    print("============================================================")
    print("============================================================")

    pilihan = input("Pilihan Menu (1-5): ")

    if pilihan == "1":
        tampilkan_data()

    elif pilihan == "2":
        tambah_data()

    elif pilihan == "3":
        ubah_data()

    elif pilihan == "4":
        hapus_data()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

        # 
data_mahasiswa = [
    ["I2610921", "Mohamad Ridho Sunami", "Ilmu Komputer"],
    ["I2610190", "Agoy", "Ilmu Komputer"],
    ["I2610115", "Archard", "Ilmu Komputer"],
    ["2610255", "Farel", "Ilmu Komputer"]
]


# Function untuk menampilkan data
def tampilkan_data():
    print("\n=== DATA MAHASISWA ===")

    if len(data_mahasiswa) == 0:
        print("Data mahasiswa masih kosong.")
    else:
        for i in range(len(data_mahasiswa)):
            mahasiswa = data_mahasiswa[i]

            print("-------------------------------------")
            print(f"Index {i}")
            print(f"NIM           : {mahasiswa[0]}")
            print(f"Nama          : {mahasiswa[1]}")
            print(f"Program Studi : {mahasiswa[2]}")
            print("-------------------------------------")


# Function untuk menambahkan data
def tambah_data():
    print("======= TAMBAH DATA MAHASISWA ========")

    nim = input("Masukkan NIM           : ")
    nama = input("Masukkan Nama          : ")
    prodi = input("Masukkan Program Studi : ")

    mahasiswa_baru = [nim, nama, prodi]

    # Menambahkan data menggunakan append
    data_mahasiswa.append(mahasiswa_baru)

    print("Data mahasiswa berhasil ditambahkan.")


# Function untuk mengubah data
def ubah_data():
    nama_mahasiswa = ["Mohamad Ridho Sunami", "Agoy", "Farel", "Archard"]

    print(nama_mahasiswa)

    index = int(input("Masukkan index yang ingin kamu ubah ya!"))
    nama_baru = input("Masukkan nama baru ya!: ")

    nama_mahasiswa[index] = nama_baru

    print("YEAY!! Data berhasil diubah")
    print(nama_mahasiswa)



# Function untuk menghapus data
def hapus_data():
    tampilkan_data()

    try:
        index = int(input("Masukkan index data yang ingin dihapus: "))

        if 0 <= index < len(data_mahasiswa):
            data_mahasiswa.pop(index)

            print("Data mahasiswa berhasil dihapus.")
        else:
            print("Index tidak ditemukan.")

    except ValueError:
        print("Index harus berupa angka.")


