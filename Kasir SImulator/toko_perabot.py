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
                        status.shelves[0].max_slot += 5  # Upgrade shelf dengan menambah kapasitas slot
                        print('Anda telah mengupgarde shelf! Kapasitas shelf sekarang:', status.shelves[0].max_slot)
                        pause()
                    else:
                        print('Uang tidak cukup untuk membeli shelf.')
                        pause()
                elif pilihan == 2:
                    if status.uang >= self.harga_perabot['kasir']:
                        status.uang -= self.harga_perabot['kasir']
                        print('Anda telah membeli kasir baru!')
                        pause()
                    else:
                        print('Uang tidak cukup untuk membeli kasir.')
                    pause()
                else:
                    print('Pilihan tidak valid. Silakan coba lagi.')
                    pause()
            except ValueError:
                print('Input tidak valid. Harap masukkan angka.')
                pause()
                continue