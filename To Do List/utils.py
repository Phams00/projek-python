import os
import json

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_task():
    if os.path.exists('list.json'):
        with open('list.json', 'r') as f:
            return json.load(f)
    return []
        
def save_task(task):
    with open('list.json', 'w') as f:
        json.dump(task, f, indent=4)

def pause():
    input('Press Enter to continue...')

def task_status(task):
    return '✓' if task.get('completed') else '✗'

def task_display(task):
    if not task:
        print('No Task Found')
        return
    for i, t in enumerate(task, 1):
        status = '✓' if t['completed'] else '✗'
        print(f'{i}. {t["task"]} [{status}] ')