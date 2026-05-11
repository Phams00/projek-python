import json
from shelf import Shelf

class Status:
    def __init__(self, waktu_game):
        self.uang = 40
        self.shelves = [Shelf()]
        self.customer_antrian = None
        self.waktu_game = waktu_game
        self.day = self.waktu_game.day

    def to_dict(self):
        return {
            'uang': self.uang,
            'shelves': [shelf.to_dict() for shelf in self.shelves],
            'day': self.day
        }

    def from_dict(self, data):
        self.uang = data.get('uang', self.uang)
        self.shelves = [Shelf.from_dict(shelf_data) for shelf_data in data.get('shelves', [])]
        self.day = data.get('day', self.day)