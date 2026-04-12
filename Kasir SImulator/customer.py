import random
from utils import clrscr, pause

class Customer:
    def __init__(self, pabrik):
        self.cart = []
        self.produk = pabrik.products
    
    def customer1(self):
        produk_terpilih = random.choices(list(self.produk.keys()), k = random.randint(1, 7))
        self.cart.extend(produk_terpilih)
        print(f"Customer memilih produk:")
        for produk in self.cart:
            print(f"- {produk}")
            
