print('PENGECEKAN STOK BARANG DI TOKO BUKU')
nama_barang = str(input('Masukan nama barang :'))
jumlah_barang = int(input('Masukan jumlah barang :'))

stok_barang = 50
if (jumlah_barang <= 50) :
    print('stok barang' , nama_barang, 'masih tersedia')
else:
    print('Stok barang', nama_barang, 'habis.')

jumlah_pengurangan = int (input('Masukan jumlah stok yang dikurangi:'))
stok_barang -= jumlah_pengurangan
print('Sisa stok barang', nama_barang, 'sekarang', stok_barang)
jumlah_tambahan = int (input('Masukan jumlah stok yang ditambahkan :'))
stok_barang += jumlah_tambahan
print('Jumlah stok', nama_barang, 'sekarang', stok_barang)


