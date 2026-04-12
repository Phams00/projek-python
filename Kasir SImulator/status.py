import json
class Status:
    def __init__(self):
        self.uang = 45
        self.barang_tersedia = []
        self.shelf1 = True
        self.shelf2 = False
        self.shelf3 = False
        self.shelf4 = False

    def to_dict(self):
        return {
            'uang': self.uang,
            'barang_tersedia': self.barang_tersedia,
            'shelf1': self.shelf1,
            'shelf2': self.shelf2,
            'shelf3': self.shelf3,
            'shelf4': self.shelf4
        }

    def from_dict(self, data):
        self.uang = data.get('uang', 45)
        self.barang_tersedia = data.get('barang_tersedia', [])
        self.shelf1 = data.get('shelf1', True)
        self.shelf2 = data.get('shelf2', False)
        self.shelf3 = data.get('shelf3', False)
        self.shelf4 = data.get('shelf4', False) 