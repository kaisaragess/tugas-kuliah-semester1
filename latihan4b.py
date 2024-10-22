#header
print("{:^44}". format("PT. DINGIN DAMAI"))
print("{:^44}". format("PROGRAM HITUNG GAJI KARYAWAN"))

#input
nama = input("\nNama Karyawan : ")
golongan = int(input("\nGolongan Jabatan\n1. 1\n2. 2\n3. 3\nPilih Golongan Anda : "))
pendidikan = input("\nPendidikan \n1. SMA\n2. D1\n3. D3\n4. S1\nPilih pendidikan terakhir Anda  : ")
jumlah_jam_kerja = int(input("\nJumlah jam kerja (satuan jam) : "))
gaji_pokok = 300000

#logika percabangan
if golongan == 1 :
    tunjangan_golongan = (0.05*gaji_pokok)
elif golongan == 2 :
    tunjangan_golongan = (0.1*gaji_pokok)
elif golongan == 3 :
    tunjangan_golongan = (0.15*gaji_pokok)
else : 
    tunjangan_golongan = 0

if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = (0.0025 * gaji_pokok) 
elif pendidikan == "D1" or pendidikan == "d1":
    tunjangan_pendidikan = (0.05 * gaji_pokok)
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = (0.2 * gaji_pokok)
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan = (0.3 * gaji_pokok)
else :
    tunjangan_pendidikan = 0

if jumlah_jam_kerja > 8 :
    gaji_lembur = ((jumlah_jam_kerja - 8)*3500 )
else :
    gaji_lembur = 0

total = gaji_pokok + tunjangan_golongan + tunjangan_pendidikan + gaji_lembur
#output
print("=================================")
print("Karyawan yang bernama ", nama)
print("Honor yang diterima")
print("     Tunjangan Jabatan Rp", tunjangan_golongan)
print("     Tunjangan Pendidikan Rp", tunjangan_pendidikan)
print("     Honor Lembur Rp", gaji_lembur)
print("     Total Gaji Rp", str(total))