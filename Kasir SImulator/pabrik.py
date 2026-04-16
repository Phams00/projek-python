from utils import clrscr, pause

class Pabrik:
    def __init__(self):
        self.products = {
            'Susu': {'harga beli': 10, 'harga jual': 14},
            'Roti': {'harga beli': 8, 'harga jual': 10},
            'Telur': {'harga beli': 15, 'harga jual': 18},
            'apel': {'harga beli': 6, 'harga jual': 9},
            'Jeruk': {'harga beli': 7, 'harga jual': 10},
            'Gula': {'harga beli': 20, 'harga jual': 27},
            'Tepung': {'harga beli': 23, 'harga jual': 30},
            'Minyak': {'harga beli': 12, 'harga jual': 18},
            'Daging': {'harga beli': 30, 'harga jual': 38},
            'Sayur': {'harga beli': 5, 'harga jual': 8},
            'Cereal': {'harga beli': 14, 'harga jual': 18},
            'Kopi': {'harga beli': 18, 'harga jual': 25},
            'Teh': {'harga beli': 18, 'harga jual': 25},
            'Air Mineral': {'harga beli': 3, 'harga jual': 5}
        }

    def tambah_produk(self, nama_produk):
        self.products[nama_produk] = 0  # Default price is 0
        print(f"Produk '{nama_produk}' telah ditambahkan ke pabrik.")

    def ui_pabrik(self, status):
        print('=============== Pabrik ===============')
        print(f'Uang: {status.uang}\n')
        print('Produk yang tersedia di pabrik:')
        for i, produk in enumerate(self.products, start=1):
            print(f'{i}, {produk} - Harga Beli: {self.products[produk]["harga beli"]}, Harga Jual: {self.products[produk]["harga jual"]}')
        print('')
        print('======================================')
        print('Masukkan angka barang yang ingin dibeli ' \
             '\natau ketik "exit" untuk kembali ke menu utama :')

    def menu_pabrik(self, status, shelf):
        while True:
            try:
                clrscr()
                self.ui_pabrik(status)
                pilihan = input('>> ')
                if pilihan.lower() == 'exit':
                    break
                elif 1 <= int(pilihan) <= len(self.products):
                    try:
                        print('ingin membeli berapa banyak?')
                        jumlah = int(input('>> '))
                        if jumlah <= 0:
                            print('Jumlah harus lebih dari 0.')
                            pause()
                            continue
                    except ValueError:
                        print('Input tidak valid. Harap masukkan angka.')
                        pause()
                        continue
                    harga_total = self.products[list(self.products.keys())[int(pilihan) - 1]]['harga beli'] * jumlah
                    print(f'Total harga untuk {jumlah} {list(self.products.keys())[int(pilihan) - 1]} adalah {harga_total}.')
                    print('Apakah Anda ingin melanjutkan pembelian? (y/n)')
                    konfirmasi = input('>> ')
                    if konfirmasi.lower() != 'y':
                        print('Pembelian dibatalkan.')
                        pause()
                        continue
                    if status.uang < harga_total:
                        print('Uang tidak cukup untuk melakukan pembelian.')
                        pause()
                        continue
                    else:
                        status.uang -= harga_total
                        produk_terpilih = list(self.products.keys())[int(pilihan) - 1]
                        shelf.tambah_ke_gudang(produk_terpilih, jumlah)
                        print(f'Anda telah membeli {jumlah} {produk_terpilih} dari pabrik.')
                        pause()
            except ValueError:
                continue
            else:
                print('Pilihan tidak valid. Silakan coba lagi.')
                pause()
        