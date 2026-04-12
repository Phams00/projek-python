import json
from shelf import Shelf

class Status:
    def __init__(self):
        self.uang = 45
        self.shelves = [Shelf()]


    def to_dict(self):
        return {
            'uang': self.uang,

        }

    def from_dict(self, data):
        self.uang = data.get('uang', 45)
        