from utils import clrscr, pause

class Pabrik:
    def __init__(self):
        self.products = {
            'Susu': 10,
            'Roti': 5,
            'Telur': 20,
            'apel': 8,
            'Jeruk': 12,
            'Gula': 15,
            'Tepung': 7,
            'Minyak': 18,
            'Daging': 25,
            'Sayur': 6,
            'Cereal': 9,
            'Kopi': 14,
            'Teh': 11,
            'Air Mineral': 4
        }
        self.barang_tersedia = []

    def tambah_produk(self, nama_produk):
        self.products[nama_produk] = 0  # Default price is 0
        print(f"Produk '{nama_produk}' telah ditambahkan ke pabrik.")