import pandas as pd
from tabulate import tabulate

class Transaction():
  def __init__(self): 
    self.cart = {}
  
  def add_item(self, item_name, item_qty, item_price):
    self.cart.update({item_name: [item_qty, item_price]})
    return print(f'{item_name} telah ditambahkan')
  
  def edit_item_name(self, item_name, new_item_name):
    self.cart.update({new_item_name: self.cart.pop(item_name)})
    return print(f'{item_name} telah diperbarui')
  
  def edit_item_qty(self, item_name, new_item_qty):
    self.cart[item_name][0] = new_item_qty
    return print(f'{item_name} telah diperbarui')
  
  def edit_item_price(self, item_name, new_item_price):
    self.cart[item_name][1] = new_item_price
    return print(f'{item_name} telah diperbarui')

  def delete_item(self, item_name):
    self.cart.pop(item_name)
    return print(f'{item_name} telah dihapus')

  def reset_trx(self):
    self.cart.clear()
    return print(f'Semua item telah dihapus')
  
  def check_order(self):
    item_value = [i for i in self.cart.values()]
    total_trx = sum([a[0]*a[1] for a in item_value])
    try:
      if total_trx > 0:
        data = pd.DataFrame(self.cart).T
        data.columns = ['Jumlah','Harga']
        print(data.to_markdown(tablefmt="grid"))
        print('Pemesanan sudah benar')
      else:
        print('Tidak ada pesanan')
    except:
      print('Lakukan reset pesanan')
  
  def price_total(self):
    item_value = [i for i in self.cart.values()]
    total_trx = sum([a[0]*a[1] for a in item_value])
    try:
      if total_trx <= 200_000:
        return print(f'Anda belanja {self.cart} dengan total belanja sebesar: {total_trx}. Belanja lebih untuk mendapatkan diskon!')
      elif total_trx > 500_000:
        total_trx = total_trx - (0.1*total_trx)
        return print(f'Anda belanja {self.cart} dan mendapatkan diskon sebesar 10%, total belanjaan anda adalah: {total_trx}')
      elif total_trx > 300_000:
        total_trx = total_trx - (0.08*total_trx)
        return print(f'Anda belanja {self.cart} dan mendapatkan diskon sebesar 8%, total belanjaan anda adalah: {total_trx}')
      elif total_trx > 200_000:
        total_trx = total_trx - (0.05*total_trx)
        return print(f'Anda belanja {self.cart} dan mendapatkan diskon sebesar 5%, total belanjaan anda adalah: {total_trx}')
    except:
      print('Periksa daftar belanja anda')