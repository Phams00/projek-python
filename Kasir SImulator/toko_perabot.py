import os
from utils import clrscr, pause

class TokoPerabot:
    def __init__(self):
        harga_perabot = {
            'shelf': 20,
            'kasir': 30
        }
    
    def ui_toko_perabot(self, status):
        print('=============== Toko Perabot ===============')
        print(f'Uang: {status.uang}\n')
        print('Perabot yang tersedia:')
        print('1. Shelf - Harga: 20')
        print('2. Kasir - Harga: 30')
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
                    if status.uang >= 20:
                        status.uang -= 20
                        print('Anda telah membeli shelf baru!')
                    else:
                        print('Uang tidak cukup untuk membeli shelf.')
                    pause()
                elif pilihan == 2:
                    if status.uang >= 30:
                        status.uang -= 30
                        print('Anda telah membeli kasir baru!')
                    else:
                        print('Uang tidak cukup untuk membeli kasir.')
                    pause()
            except ValueError:
                print('Input tidak valid. Harap masukkan angka.')
                pause()
                continue