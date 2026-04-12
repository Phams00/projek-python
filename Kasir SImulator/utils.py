import os
import json

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input()
def load_task():
    if os.path.exists('list.json'):
        with open('list.json', 'r') as f:
            return json.load(f)
    return []
        
def save_task(task):
    with open('list.json', 'w') as f:
        json.dump(task, f, indent=4)