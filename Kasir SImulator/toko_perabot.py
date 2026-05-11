import os
from utils import clrscr, pause
from shelf import Shelf

class TokoPerabot:
    def __init__(self):
        harga_perabot = {
            'shelf': 20,
            'kasir': 30
        }
        self.harga_perabot = harga_perabot
        self.shelf = Shelf()

    def ui_toko_perabot(self, status):
        print('=============== Toko Perabot ===============')
        print(f'Uang: {status.uang}\n')
        print('Perabot yang tersedia:')
        print(f'1. Upgrade Shelf - Harga: {self.harga_perabot["shelf"]}')
        print(f'2. Kasir - Harga: {self.harga_perabot["kasir"]}')
        print('0. Kembali ke menu utama')
        print('============================================')
        print('Masukkan pilihan:')

    def menu_toko_perabot(self, status):
        while True:
            try:
                clrscr()
                self.ui_toko_perabot(status)
                pilihan = int(input('>> '))
                if pilihan == 0:
                    break
                elif pilihan == 1:
                    if status.uang >= self.harga_perabot['shelf']:
                        status.uang -= self.harga_perabot['shelf']
                        self.shelf.max_slot += 5  # Menambah kapasitas shelf
                        print('Anda telah mengupgarde shelf! Kapasitas shelf sekarang:', self.shelf.max_slot)
                    else:
                        print('Uang tidak cukup untuk membeli shelf.')
                    pause()
                elif pilihan == 2:
                    if status.uang >= self.harga_perabot['kasir']:
                        status.uang -= self.harga_perabot['kasir']
                        print('Anda telah membeli kasir baru!')
                    else:
                        print('Uang tidak cukup untuk membeli kasir.')
                    pause()
            except ValueError:
                print('Input tidak valid. Harap masukkan angka.')
                pause()
                continue