import os
from collections import Counter
from utils import clrscr, pause

class Shelf:
    def __init__(self):
        self.slot = []
        self.max_slot = 10
        self.gudang = {}

    def tambah_ke_gudang(self, nama_produk, jumlah):
        if nama_produk in self.gudang:
            self.gudang[nama_produk] += jumlah
        else:
            self.gudang[nama_produk] = jumlah

    def pindahkan_ke_shelf(self, nama_produk, jumlah):
        if nama_produk not in self.gudang:
            print(f"Produk '{nama_produk}' tidak tersedia di gudang.")
            pause()
            return
        if self.gudang[nama_produk] < jumlah:
            print(f"Stok '{nama_produk}' di gudang tidak cukup.")
            pause()
            return
        if len(self.slot) + jumlah > self.max_slot:
            print('shelf penuh, tidak bisa menambah produk lagi')
            pause()
            return
        self.gudang[nama_produk] -= jumlah
        if self.gudang[nama_produk] == 0:
            del self.gudang[nama_produk]
        self.slot.extend([nama_produk] * jumlah)

    def ambil_dari_shelf(self, nama_produk, jumlah):
        if nama_produk not in self.slot: # Cek apakah produk ada di shelf
            print(f"Produk '{nama_produk}' tidak tersedia di shelf.")
            pause()
            return
        if self.slot.count(nama_produk) < jumlah: # Menggunakan count untuk menghitung jumlah produk di shelf
            print(f"Stok '{nama_produk}' di shelf tidak cukup.")
            pause()
            return
        for _ in range(jumlah):
            self.slot.remove(nama_produk)

    def cek_slot(self):
        return self.max_slot - len(self.slot)
    
    def tampilkan_shelf(self):
        print('=============== Isi Shelf ===============')
        print('')
        isi = Counter(self.slot)
        for produk, jumlah in isi.items():
            print(f'- {produk} x{jumlah}')
        print(f'sisa slot: {self.cek_slot()}')

        print('\n=============== Isi Gudang =============')
        print('')
        for produk, jumlah in self.gudang.items():
            print(f'- {produk} x{jumlah}')

    def ui_menu_shelf(self):
        print('=============== Menu Shelf ===============\n')
        print('1. lihat isi shelf dan gudang')
        print('2. Masukkan produk ke dalam shelf')
        print('0. Kembali ke menu utama')
        print('\n=========================================\n')
        print('Pilih menu: ')

    def menu_shelf(self):
        while True:
            clrscr()
            self.ui_menu_shelf()
            pilihan = input('>> ')
            if pilihan == '1':
                self.tampilkan_shelf()
                pause()
            elif pilihan == '2':
                for i, produk in enumerate(self.gudang.keys(), start=1):
                    print(f'{i}. {produk} - Stok: {self.gudang[produk]}')
                print()
                try:
                    print('Pilih produk yang ingin dimasukkan ke shelf:')
                    pilihan_produk = int(input('>> '))
                    if 1 <= pilihan_produk <= len(self.gudang):
                        nama_produk = list(self.gudang.keys())[pilihan_produk - 1]
                        print(f'Berapa banyak {nama_produk} yang ingin dimasukkan ke shelf?')
                        jumlah = int(input('>> '))
                        self.pindahkan_ke_shelf(nama_produk, jumlah)
                    else:
                        print('Pilihan tidak valid.')
                        pause()
                except ValueError:
                    print('Input tidak valid. Harap masukkan angka.')
                    pause()
            elif pilihan == '0':
                break
        
