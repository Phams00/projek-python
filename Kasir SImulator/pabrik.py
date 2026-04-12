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
        print()