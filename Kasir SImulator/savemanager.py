import json
import os
from shelf import Shelf

def save(status, waktu_game):
    data = {
        'uang': status.uang,
        'day': waktu_game.day,
        "shelves": [shelf.to_dict() for shelf in status.shelves]
    }
    with open('savefile.json', 'w') as f:
        json.dump(data, f, indent=4)

def load(status, waktu_game):
    if not os.path.exists('savefile.json'):
        return False
    with open('savefile.json', 'r') as f:
        data = json.load(f)
    status.uang = data.get('uang')
    waktu_game.day = data.get('day')
    status.shelves = [Shelf.from_dict(s) for s in data.get('shelves', [])]
    return True
    
def reset_game():
    if os.path.exists('savefile.json'):
        os.remove('savefile.json')