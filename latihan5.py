#header
print('''
      GEROBAK FRIED CHICKEN
----------------------------------
Kode     Jenis Potong        Harga
----------------------------------
D        Dada                Rp2.500
P        Paha                Rp2.000
S        Sayap               Rp1.500
----------------------------------''')

#inisiasi variabel
jenis_potong = []
harga_satuan = []
byk_beli = []
jumlah_harga = []

#proses
byk_pesanan = int(input("banyak pesanan = "))

for i in range(byk_pesanan) :
    print("Pesanan Ke - ",i+1)
    input_kd_ptg = input("Kode Potong (D/P/S) = ")

    if input_kd_ptg == "D" :
        jenis_potong.append(input_kd_ptg)
        harga_satuan.append(2500)
    elif input_kd_ptg == "P" :
        jenis_potong.append(input_kd_ptg)
        harga_satuan.append(2000)
    elif input_kd_ptg == "S" :
        jenis_potong.append(input_kd_ptg)
        harga_satuan.append(1500)
    
    byk_beli.append(input("Banyak Potong = "))

for j in range(byk_pesanan) :
    jumlah_harga.append((float(harga_satuan[j]))*(float(byk_beli[j])))

#output
print('''
===================================================================================
No.     JenisPotong     HargaSatuan     BanyakBeli      JumlahHarga
===================================================================================
''')

for k in range(byk_pesanan) :
    print("%s \t %s \t\t %s \t\t %s \t\t Rp%s" % (k+1, jenis_potong[k], harga_satuan[k], byk_beli[k], jumlah_harga[k]))

print("====================================================================================")

jumlah_bayar = 0

for l in range(len(jumlah_harga)) :
    jumlah_bayar = jumlah_bayar + float(jumlah_harga[l])

print("Jumlah bayar Rp", str(jumlah_bayar))
print("Pajak 10 % Rp", str(jumlah_bayar*0.1))
print("Total Bayar Rp", str((jumlah_bayar)+(jumlah_bayar*0.1)))