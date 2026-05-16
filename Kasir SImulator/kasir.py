import os
from utils import clrscr, pause, wait

class Kasir:
    def __init__(self, status, pabrik):
        self.status = status
        self.pabrik = pabrik

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
                    wait(2.5)
                    break
                print('[Layani customer!]')
                print('Tekan Enter untuk menyelesaikan transaksi...')
                input()
                total_harga = sum([self.pabrik.products[item]['harga jual'] for item in customer.cart])
                self.status.uang += total_harga
                print(f'Transaksi selesai! Total harga: {total_harga}. Uang sekarang: {self.status.uang}')
                customer.cart.clear()
                self.status.customer_antrian = None
                pause()
                break

            except ValueError:
                continue
