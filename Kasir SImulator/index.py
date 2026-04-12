import os
import random
import time
import json
import threading
from utils import clrscr, pause  
from pabrik import Pabrik
from customer import Customer
from status import Status
from gametime import waktu
from shelf import Shelf

status = Status()
pabrik = Pabrik(status.shelves[0])
waktu_game = waktu()

timer_thread = threading.Thread(target=waktu_game.jalankan_timer)
timer_thread.daemon = True
timer_thread.start()


def ui_main():
    print("=== Selamat Datang di Kasir Simulator ===")
    print(f'Hari ke-{waktu_game.get_day()} | Uang: {status.uang}')
    print(f'Sisa Waktu: {waktu_game.format_time(waktu_game.sisa_waktu())}', end='\n\n')
    print('')
    print("Menu:")
    print("1. Pergi ke pabrik (tambah produk)")
    print("2. Lihat Produk yang tersedia di toko (cek isi shelf)")
    print("3. Pergi ke kasir (checkout)")
    print("0. Keluar")

    print("=========================================")

def main():
    while True:
        try:
            clrscr()
            ui_main()
            choice = input("Pilih menu: ")
            
            if choice == '1':
                pabrik.menu_pabrik(status)
            elif choice == '2':
                status.shelves[0].menu_shelf()
            elif choice == '0':
                print("Terima kasih telah menggunakan Kasir Simulator!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()