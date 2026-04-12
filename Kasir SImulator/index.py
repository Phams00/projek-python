import os
import random
import time
import json
from utils import clrscr, pause, load_task, save_task
from pabrik import Pabrik
from customer import Customer
from status import Status
from gametime import waktu

status = Status()
pabrik = Pabrik()
time = waktu()

def ui_main():
    print("=== Selamat Datang di Kasir Simulator ===")
    print(f'Hari ke-{time.get_day()} | Uang: {status.uang}')
    print(f'Sisa Waktu: {time.format_time(time.sisa_waktu())}', end='\n\n')
    print('')
    print("Menu:")
    print("1. Pergi ke pabrik (tambah produk)")
    print("2. Lihat Produk yang tersedia di toko (cek isi shelf)")
    print("3. Pergi ke kasir (checkout)")

    print("=========================================")

def main():
    while True:
        try:
            ui_main()
            choice = input("Pilih menu: ")
            
            if choice == '1':
                print("Fitur tambah produk belum tersedia.")
                input("Tekan Enter untuk melanjutkan...")
            elif choice == '2':
                print("Fitur lihat produk belum tersedia.")
                input("Tekan Enter untuk melanjutkan...")
            elif choice == '3':
                print("Terima kasih telah menggunakan Kasir Simulator!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Tekan Enter untuk melanjutkan...")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()