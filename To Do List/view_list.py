import os
import json
from utils import clrscr, load_task, pause, task_display

class ViewList:
    def __init__(self):
        pass
    
    def view(self):
        try:
            while True:
                clrscr()
                print("==================")
                print('     To Do List')
                print("==================")
                task = load_task()
                if not task:
                    print('No Task Found')
                    print('Press Enter to return')
                    input()
                    break
                else:
                    with open('list.json', 'r') as f:
                        task = json.load(f)
                    task_display(task)
                    print('==================')
                    pause()
                    break
        except KeyboardInterrupt:
            print('')