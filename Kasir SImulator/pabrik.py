from utils import clrscr, pause

class Pabrik:
    def __init__(self):
        self.products = {
            'Susu': {'harga beli': 10, 'harga jual': 20},
            'Roti': {'harga beli': 10, 'harga jual': 20},
            'Telur': {'harga beli': 10, 'harga jual': 20},
            'apel': {'harga beli': 10, 'harga jual': 20},
            'Jeruk': {'harga beli': 10, 'harga jual': 20},
            'Gula': {'harga beli': 10, 'harga jual': 20},
            'Tepung': {'harga beli': 10, 'harga jual': 20},
            'Minyak': {'harga beli': 10, 'harga jual': 20},
            'Daging': {'harga beli': 10, 'harga jual': 20},
            'Sayur': {'harga beli': 10, 'harga jual': 20},
            'Cereal': {'harga beli': 10, 'harga jual': 20},
            'Kopi': {'harga beli': 10, 'harga jual': 20},
            'Teh': {'harga beli': 10, 'harga jual': 20},
            'Air Mineral': {'harga beli': 10, 'harga jual': 20}
        }
        self.barang_tersedia = []

    def tambah_produk(self, nama_produk):
        self.products[nama_produk] = 0  # Default price is 0
        print(f"Produk '{nama_produk}' telah ditambahkan ke pabrik.")

    def ui_pabrik(self):
        print('=============== Pabrik ===============')
        print('Produk yang tersedia di pabrik:')
        for i, produk in enumerate(self.products, start=1):
            print(f'{i}, {produk} - Harga Beli: {self.products[produk]["harga beli"]}, Harga Jual: {self.products[produk]["harga jual"]}')
        print('')
        print('======================================')
        print('Masukkan angka barang yang ingin dibeli ' \
             '\natau ketik "exit" untuk kembali ke menu utama :')

    def menu_pabrik(self, status):
        while True:
            clrscr()
            self.ui_pabrik()
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
                status.uang -= harga_total
                produk_terpilih = list(self.products.keys())[int(pilihan) - 1]
                self.barang_tersedia.append(produk_terpilih)
                print(f'Anda telah membeli {produk_terpilih} dari pabrik.')
                pause()
            else:
                print('Pilihan tidak valid. Silakan coba lagi.')
                pause()
        