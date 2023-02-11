from cashier import Transaction

trx = Transaction()

while True:
  print('\nPython Super Cashier')
  print(' ')
  print('1. Tambahkan Barang')
  print('2. Edit Nama Barang')
  print('3. Edit Jumlah Barang')
  print('4. Edit Harga Barang')
  print('5. Hapus Barang')
  print('6. Kosongkan Keranjang')
  print('7. Lihat Keranjang')
  print('8. Checkout Barang')
  print('9. Selesai\n')

  try:
    entry = int(input('Masukkan pilihan : '))
    if entry == 1:
      nama = str(input('Nama Barang : '))
      jumlah = int(input('Jumlah Barang : '))
      harga = int(input('Harga Barang : '))
      trx.add_item(nama, jumlah, harga)

    elif entry == 2:
      edit_nama = str(input('Nama barang yang ingin dirubah : '))
      new_nama = str(input('Masukkan nama barang yang baru : '))
      trx.edit_item_name(edit_nama, new_nama)

    elif entry == 3:
      edit_jumlah = str(input('Nama barang yang ingin dirubah : '))
      new_jumlah = str(input('Masukkan jumlah barang yang baru : '))
      trx.edit_item_qty(edit_nama, new_jumlah)

    elif entry == 4:
      edit_harga = str(input('Nama barang yang ingin dirubah : '))
      new_harga = str(input('Masukkan harga barang yang baru : '))
      trx.edit_item_name(edit_nama, new_harga)

    elif entry == 5:
      hps = str(input('Nama barang yang ingin dihapus : '))
      trx.delete_item(hps)

    elif entry == 6:
      trx.reset_trx()

    elif entry == 7:
      trx.check_order()

    elif entry == 8:
      trx.price_total()
      break

    elif entry == 9:
      break
  
  except ValueError:
    print('Tidak ada pilihan')