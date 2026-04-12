import json
from shelf import Shelf

class Status:
    def __init__(self):
        self.uang = 40
        self.shelves = [Shelf()]
        self.customer_antrian = None


    def to_dict(self):
        return {
            'uang': self.uang,
            'shelves': [shelf.to_dict() for shelf in self.shelves],
        }

    def from_dict(self, data):
        self.uang = data.get('uang', 45)
        self.shelves = [Shelf.from_dict(shelf_data) for shelf_data in data.get('shelves', [])]