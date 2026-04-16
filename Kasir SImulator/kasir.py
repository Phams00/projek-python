import os
from utils import clrscr, pause

class Kasir:
    def __init__(self, status):
        self.status = status

    def ui_menu_kasir(self, customer):
        print('=============== Kasir ===============')
        print(f'Uang: {self.status.uang}\n')
        if self.status.customer_antrian is not None:
            print('Customer ingin membeli barang berikut:')
            for item in customer.cart:
                print(f'- {item}')
        else:
            print('Belum ada customer')
        print('======================================')

    def menu_kasir(self, customer):
        while True:
            try:
                clrscr()
                self.ui_menu_kasir(customer)
                if self.status.customer_antrian is None:
                    print('Tidak ada customer di kasir. Kembali ke menu utama...')
                    pause()
                    break
                print('[Layani customer!]')
                print('Tekan Enter untuk menyelesaikan transaksi...')
                input()
                total_harga = sum([self.status.shelves[0].gudang.get(item, 0) for item in customer.cart])
                self.status.uang += total_harga
                print(f'Transaksi selesai! Total harga: {total_harga}. Uang sekarang: {self.status.uang}')
                customer.cart.clear()

            except ValueError:
                continue
