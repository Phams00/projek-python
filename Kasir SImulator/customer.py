import random
from utils import clrscr, pause
from shelf import Shelf

class Customer:
    def __init__(self, pabrik, status):
        self.cart = []
        self.produk = pabrik.products
        self.status = status

    def coba_muncul(self):
        shelf = self.status.shelves[0]
        if not shelf.slot:
            return False
        change = len(shelf.slot) / shelf.max_slot
        return random.random() < change
    
    def customer1(self):
        produk_terpilih = random.choices(list(self.produk.keys()), k = random.randint(1, 7))
        self.cart.extend(produk_terpilih)
        print(f"Customer memilih produk:")
        for produk in self.cart:
            print(f"- {produk}")
            
