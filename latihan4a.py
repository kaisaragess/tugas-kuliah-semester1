#header
print("====================================================")
print("{:^50}". format("Pendaftaran Mahasiswa Baru"))
print("====================================================")

#input
nis = int(input("NIS : "))
nama = input("Masukkan Nama : ")
jurusan = input("Pilihan prodi \n1. Sistem Informasi (SI) \n2. Sistem Informasi Akuntansi (SIK)\nTuliskan pilihanmu : ")


#Logika Percabangan
if jurusan == "Sistem Informasi" or "sistem informasi" or "si" or "SI":
    KodeProdi = "SI"
    NamaProdi   = "Sistem Informasi"
    Harga = 2400000
elif jurusan == "Sistem Informasi Akuntansi" or "sistem informasi akuntansi" or "sik" or "SIK" :
    KodeProdi = "SIA"
    NamaProdi   = "Sistem informasi Akuntansi"
    Harga = 2000000
else :
    print("Jurusan anda tidak ada di list")

#output
print("====================================================")
print("Nomor Induk Siswa        : ", nis)
print("Nama                     : ", nama)
print("Kode Prodi               : ", KodeProdi)
print("Nama Prodi               : ", NamaProdi)
print("Harga                    : ", Harga)