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
from kasir import Kasir

status = Status()
shelf = status.shelves[0]
pabrik = Pabrik()
waktu_game = waktu()
customer = Customer(pabrik, status)
gamekasir = Kasir(status)

timer_thread = threading.Thread(target=waktu_game.jalankan_timer)
timer_thread.daemon = True
timer_thread.start()

customer_thread = threading.Thread(target=customer.jalankan_customer)
customer_thread.daemon = True
customer_thread.start()


def ui_main():
    print("=== Selamat Datang di Kasir Simulator ===")
    print(f'Hari ke-{waktu_game.get_day()} | Uang: {status.uang}')
    print(f'Sisa Waktu: {waktu_game.format_time(waktu_game.sisa_waktu())}', end='\n\n')
    print('')
    print("Menu:")
    print("1. Pergi ke pabrik (tambah produk)")
    print("2. Lihat Produk yang tersedia di toko (cek isi shelf)")
    print("3. Pergi ke kasir (checkout)")
    print('4. Pergi ke Toko perabot')
    print("0. Keluar (save & exit)")

    print("=========================================")

def main():
    while True:
        try:
            clrscr()
            ui_main()
            choice = input("Pilih menu: ")
            
            if choice == '1':
                pabrik.menu_pabrik(status, shelf)
            elif choice == '2':
                shelf.menu_shelf()
            elif choice == '3':
                gamekasir.menu_kasir(customer)
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