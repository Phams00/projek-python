import random
import time
from utils import clrscr, pause
from shelf import Shelf

class Customer:
    def __init__(self, pabrik, status):
        self.cart = []
        self.produk = pabrik.products
        self.status = status

    def coba_muncul(self):  #persen muncul customer dengan menggunakan jumlah slot yang terisi
        shelf = self.status.shelves[0]
        if not shelf.slot:
            return False
        change = len(shelf.slot) / shelf.max_slot
        return random.random() < change

    def pilih_barang(self):
        shelf = self.status.shelves[0]
        barang_terpilih = random.choices(shelf.slot, k = random.randint(1, 7))
        for i in barang_terpilih:
            shelf.ambil_dari_shelf(i, 1)
        self.cart.extend(barang_terpilih)
            
    def jalankan_customer(self):
        while True:
            time.sleep(10)
            if self.status.customer_antrian is None:
                if self.coba_muncul():
                    self.pilih_barang()
                    self.status.customer_antrian = self
                    print("\n [!] Ada Customer Di Kasir")